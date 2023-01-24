from io import BytesIO
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


name= 'HomeSP_take100'
fqcn = CompositeName(NAMESPACE_DEFAULT, NAME_EXACT, name)


meta =  {'itemtype': 'default',
         'contenttype': 'text/x-markdown;charset=utf-8',
         'namespace': NAMESPACE_DEFAULT,
         'summary': 'summary 9',
         'name': [name],
         'tags': ['sfsd sfsfh tha3'],
         'comment': 'mycomment9',
         }

data = b"this si same string text;convereted to bytes and then to BytesIO"
revid = storage_routing.store(meta, data)
storage_routing.commit()
print ("revid =", revid)
content =  indexes.indexible_content(meta, data, is_new = True)
itemtype =  'default'
contenttype =  'text/x-markdown;charset=utf-8'
wikiitem = WikiItem.create(fqcn, itemtype=itemtype, contenttype=contenttype)
# storage_revid would be put by 
#meta[REVID] = revid 

indexes.save(wikiitem, meta, data,  storage_revid = revid)


# check if item is saved in the index
whoosh_doc = indexes.document_search(**fqcn.query_terms)
print ("whoosh_doc = ", whoosh_doc)
