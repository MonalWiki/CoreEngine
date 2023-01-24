from io import BytesIO
import os
from wikicoreengine.wikicfg import NAMESPACES, WIKINAME, BACKEND_DATADIR_BASE
from wikicoreengine.data.storage_routing import storage_routing
from wikicoreengine.data.indexes import indexes, get_storage_revision # 

from wikicoreengine.constant_keys import NAME, NAMESPACE, NAME_EXACT, NAMESPACE_DEFAULT, CURRENT, CONTENTTYPE, REVID
from wikicoreengine.constant_keys import MTIME, PTIME, ITEMID, LATEST_REVS, NAME_EXACT, UFIELDS, REVID, CONTENTTYPE, CURRENT, ITEMTYPE, ITEMTYPE_DEFAULT, ITEMTYPE_NONEXISTENT


from wikicoreengine.Name import CompositeName, url_to_compositeName
from wikicoreengine.contenttypes import CONTENTTYPE_NONEXISTENT, CONTENTTYPE_DEFAULT, CONTENTTYPE_MARKDOWN
from wikicoreengine.item import WikiItem
from wikicoreengine.frontend import view_function



from wikicoreengine.dependencies import Container
from dependency_injector import containers, providers

def startup_func():
    print ("startup func called")
    storage_base_dir = f"{BACKEND_DATADIR_BASE}/{WIKINAME}"
    storage_routing(NAMESPACES, storage_base_dir)
    indexes(storage_base_dir)
    pass


# container = Container()
# container.app_builder.override(providers.Callable(jp.build_app,
#                                                   startup_func = startup_func
#                                                   )
#                                )

    
# container.wire(modules=[view_function])
# view_function.set_app() # dependency already injected
view_function.build_app(startup_func = startup_func)
app = view_function.app
from starlette.testclient import TestClient
with TestClient(view_function.app) as client:
    response = client.get('/HomeSP_take7')
