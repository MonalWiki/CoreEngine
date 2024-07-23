"""
Populate wiki with a markdown page when  offline, i.e, when server is turned off.
Allows wiki to be used like blog.

"""
import logging    
import os
from wikicoreengine.wikicfg import NAMESPACES, WIKINAME, BACKEND_DATADIR_BASE
from wikicoreengine.data.storage_routing import storage_routing
from wikicoreengine.data.indexes import indexes

from wikicoreengine.constant_keys import NAME, NAMESPACE, NAME_EXACT, NAMESPACE_DEFAULT, CURRENT, CONTENTTYPE, REVID
from wikicoreengine.Name import CompositeName
from wikicoreengine.item import WikiItem

storage_base_dir = f"{BACKEND_DATADIR_BASE}/{WIKINAME}"
storage_routing(NAMESPACES, storage_base_dir)
indexes(storage_base_dir)

logger = logging.getLogger(__name__)
def add_md_item_to_wiki(name, tags, summary, comment, md_content):
    fqcn = CompositeName(NAMESPACE_DEFAULT, NAME_EXACT, name)
    meta =  {'itemtype': 'default',
             'contenttype': 'text/x-markdown;charset=utf-8',
             'namespace': NAMESPACE_DEFAULT,
             'summary': summary,
             'name': [name],
             'tags': tags,
             'comment': comment,
             }
    data = md_content.encode('utf-8')
    revid = storage_routing.store(meta, data)
    storage_routing.commit()
    logger.info(f"adding item with name = {name} to storage; revid={revid}")
    content =  indexes.indexible_content(meta, data, is_new = True)
    itemtype =  'default'
    contenttype =  'text/x-markdown;charset=utf-8'
    wikiitem = WikiItem.create(fqcn, itemtype=itemtype, contenttype=contenttype)
    indexes.save(wikiitem, meta, data,  storage_revid = revid)
    # check if item is saved in the index
    whoosh_doc = indexes.document_search(**fqcn.query_terms)
    print ("whoosh_doc = ", whoosh_doc)


def overwrite_wiki_content(name, tag, summary, comment, md_content):
    """
    a wiki item already exists -- replace with new content
    """
    fqcn = CompositeName(NAMESPACE_DEFAULT, NAME_EXACT, name)
    # search for existing doc
    whoosh_doc = indexes.document_search(**fqcn.query_terms)

    # retrieve existing 
    meta, data = storage_routing.retrieve(NAMESPACE_DEFAULT, whoosh_doc['revid'])

    # replace the content in sqlite dbstore
    storage_routing.update_item(NAMESPACE_DEFAULT, whoosh_doc['dataid'], md_content)
    # remove existing index
    indexes.remove_revision(whoosh_doc['revid'])
    itemtype =  'default'
    contenttype =  'text/x-markdown;charset=utf-8'
    wikiitem = WikiItem.create(fqcn, itemtype=itemtype, contenttype=contenttype)
    indexes.save(wikiitem, meta, data,  storage_revid = whoosh_doc['revid'])
