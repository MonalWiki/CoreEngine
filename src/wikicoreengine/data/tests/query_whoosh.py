from io import BytesIO
import os
from wikicoreengine.wikicfg import NAMESPACES, WIKINAME, BACKEND_DATADIR_BASE
from wikicoreengine.data.storage_routing import storage_routing
from wikicoreengine.data.indexes import indexes

from wikicoreengine.constant_keys import NAME, NAMESPACE, NAME_EXACT, NAMESPACE_DEFAULT, CURRENT, CONTENTTYPE, REVID
from wikicoreengine.Name import CompositeName
from wikicoreengine.wiki import WikiItem

storage_base_dir = f"{BACKEND_DATADIR_BASE}/{WIKINAME}"
# storage backend 
storage_routing(NAMESPACES, storage_base_dir)
# init indexes 
indexes(storage_base_dir)
fqcn = CompositeName(NAMESPACE_DEFAULT, NAME_EXACT, 'ItemWiththisNameDoesNotExists')
index_item = indexes.create(**fqcn.query_terms)
print (type(index_item))

print (index_item.query)

print (index_item.current)
