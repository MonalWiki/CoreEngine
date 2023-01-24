from io import BytesIO
import os
from wikicoreengine.wikicfg import NAMESPACES, WIKINAME, BACKEND_DATADIR_BASE
from wikicoreengine.data.storage_routing import storage_routing
from wikicoreengine.data.indexes import indexes, get_storage_revision # 

from wikicoreengine.constant_keys import NAME, NAMESPACE, NAME_EXACT, NAMESPACE_DEFAULT, CURRENT, CONTENTTYPE, REVID
from wikicoreengine.constant_keys import MTIME, PTIME, ITEMID, LATEST_REVS, NAME_EXACT, UFIELDS, REVID, CONTENTTYPE, CURRENT, ITEMTYPE, ITEMTYPE_DEFAULT, ITEMTYPE_NONEXISTENT


from wikicoreengine.Name import CompositeName, url_to_compositeName
from wikicoreengine.contenttypes import CONTENTTYPE_NONEXISTENT, CONTENTTYPE_DEFAULT, CONTENTTYPE_MARKDOWN

storage_base_dir = f"{BACKEND_DATADIR_BASE}/{WIKINAME}"
# storage backend 
storage_routing(NAMESPACES, storage_base_dir)
# init indexes 
indexes(storage_base_dir)


item_name = "ItemV2"
fqcn = url_to_compositeName(item_name)
itemtype = ITEMTYPE_NONEXISTENT
contenttype = None
rev_id = None
rev = get_storage_revision(fqcn, itemtype, contenttype, rev_id)
print ("rev = ", rev)
