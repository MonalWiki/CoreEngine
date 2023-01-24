from ..wikicfg import NAMESPACES, WIKINAME, BACKEND_DATADIR_BASE
from ..data.storage_routing import storage_routing
from ..data import indexes, get_storage_revision

# all kinds of nice middlewares will go here
def startup_func():
    print ("startup func called")
    storage_base_dir = f"{BACKEND_DATADIR_BASE}/{WIKINAME}"
    storage_routing(NAMESPACES, storage_base_dir)
    indexes(storage_base_dir)
    pass
