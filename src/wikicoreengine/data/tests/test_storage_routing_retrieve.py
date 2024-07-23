from io import BytesIO
import os
from wikicoreengine.wikicfg import NAMESPACES, WIKINAME, BACKEND_DATADIR_BASE
from wikicoreengine.data.storage_routing import storage_routing

from wikicoreengine.constant_keys import NAME, NAMESPACE, NAME_EXACT, NAMESPACE_DEFAULT, CURRENT, CONTENTTYPE, REVID
from wikicoreengine.Name import CompositeName
from wikicoreengine.data.indexes import indexes


storage_base_dir = f"{BACKEND_DATADIR_BASE}/{WIKINAME}"
storage_base_dir = f"{BACKEND_DATADIR_BASE}/{WIKINAME}"
storage_routing(NAMESPACES, storage_base_dir)
indexes(storage_base_dir)


# storage backend
name = "Home2"

fqcn = CompositeName(NAMESPACE_DEFAULT, NAME_EXACT, name)
whoosh_doc = indexes.document_search(**fqcn.query_terms)

meta, data = storage_routing.retrieve(NAMESPACE_DEFAULT, whoosh_doc['revid'])

print ("data = ", data)
print ("content = ", whoosh_doc['content'])




