"""
search for non-existent item in index -- returns None

"""

from io import BytesIO
import os

from wikicoreengine.wikicfg import NAMESPACES, WIKINAME, BACKEND_DATADIR_BASE
from wikicoreengine.data.storage_routing import storage_routing
from wikicoreengine.data.indexes import indexes

from wikicoreengine.constant_keys import NAME, NAMESPACE, NAME_EXACT, NAMESPACE_DEFAULT, CURRENT, CONTENTTYPE
from wikicoreengine.Name import CompositeName

storage_base_dir = f"{BACKEND_DATADIR_BASE}/{WIKINAME}"
# init storage backend 
storage_routing(NAMESPACES, storage_base_dir)
# init indexes 
indexes(storage_base_dir)

# the fqcn
fqcn = CompositeName(NAMESPACE_DEFAULT, NAME_EXACT, 'ekitem')

# search index for fqcn 
# in moin -- ProtectingMiddleware.get_item is called ; which calls Indexing.get_item
# which creates an Item object, which calls indexer._document which picks up the
# Whoosh index-seracher which call returns searcher.document

# here we directly call indexes.document_search 
index_item = indexes.document_search(**fqcn.query_terms)
print (index_item)
print (type(index_item))

