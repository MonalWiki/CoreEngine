# first get the whoosh_doc from item_name

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


name = "Home2"
fqcn = CompositeName(NAMESPACE_DEFAULT, NAME_EXACT, name)
whoosh_doc = indexes.document_search(**fqcn.query_terms)

print (whoosh_doc['revid'])

# get the data

meta, data = storage_routing.retrieve(NAMESPACE_DEFAULT, whoosh_doc['revid'])
#print ("meta = ",  meta)

print ("data = ", data)

new_data = b"""
# This is new new text
## Lets se if it goes through
"""


storage_routing.update_item(NAMESPACE_DEFAULT, whoosh_doc['dataid'], new_data)
# don't commit


indexes.remove_revision(whoosh_doc['revid'])

# now update the indexes

itemtype =  'default'
contenttype =  'text/x-markdown;charset=utf-8'
wikiitem = WikiItem.create(fqcn, itemtype=itemtype, contenttype=contenttype)
indexes.save(wikiitem, meta, data,  storage_revid = whoosh_doc['revid'])

# search the same doc
whoosh_doc = indexes.document_search(**fqcn.query_terms)

# and look for content
print (whoosh_doc['content'])

# meta, data = storage_routing.retrieve(NAMESPACE_DEFAULT, whoosh_doc['revid'])
# print ("meta = ",  meta)

# print ("data = ", data)

#storage_routing.commit()


