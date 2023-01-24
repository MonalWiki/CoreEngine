import os
#import indexes

from wikicoreengine.wikicfg import (BACKEND_DATADIR_BASE,
                                    WIKINAME,
                                    NAMESPACES,
                                    STORAGETYPE,
                                    STORAGEARGS)

from storage import StorageType, create_storage
import sys
def build_dir(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

build_dir(BACKEND_DATADIR_BASE)
build_dir(f"{BACKEND_DATADIR_BASE}/{WIKINAME}")
def build_namespace_storage(namespace):
    storage_base_dir = f"{BACKEND_DATADIR_BASE}/{WIKINAME}/{namespace}"
    build_dir(storage_base_dir)
    create_storage(storage_base_dir,  STORAGETYPE, STORAGEARGS)
    pass

    
for namespace in NAMESPACES:
    build_namespace_storage(namespace)


