"""
tests creation of indexQueryAnswer which is the structure retured by
indexes.create. 
"""
from io import BytesIO
import os
from wikicoreengine.wikicfg import NAMESPACES, WIKINAME, BACKEND_DATADIR_BASE
from wikicoreengine.data.storage_routing import storage_routing
from wikicoreengine.data.indexes import indexes

from wikicoreengine.constant_keys import NAME, NAMESPACE, NAME_EXACT, NAMESPACE_DEFAULT, CURRENT, CONTENTTYPE, REVID
from wikicoreengine.Name import CompositeName
from wikicoreengine.item import WikiItem

storage_base_dir = f"{BACKEND_DATADIR_BASE}/{WIKINAME}"
# storage backend 
storage_routing(NAMESPACES, storage_base_dir)
# init indexes 
indexes(storage_base_dir)
# fqcn = CompositeName(NAMESPACE_DEFAULT, NAME_EXACT, 'ItemWiththisNameDoesNotExists')
# index_queryAnswer = indexes.create(**fqcn.query_terms)
# print (type(index_queryAnswer))
# print (index_queryAnswer.query)
# print (index_queryAnswer.answer)

# add a item to indexes

meta =  {'itemtype': 'default',
         'contenttype': 'text/x-markdown;charset=utf-8',
         'namespace': NAMESPACE_DEFAULT,
         'summary': 'summary 9',
         'name': ['Home3'],
         'tags': ['sfsd sfsfh tha3'],
         'comment': 'mycomment9',
         'rev_number': 1}

data = b"# Hello\n## HELLOHELLO"
revid = storage_routing.store(meta, data)
meta[REVID] = revid
content = indexes.indexible_content(meta, data)
print("indexible content = ", content)
indexes.index_revision(meta, content) # 
fqcn = CompositeName(NAMESPACE_DEFAULT, NAME_EXACT, 'Home3')
index_queryAnswer = indexes.create(**fqcn.query_terms)
print(index_queryAnswer)
