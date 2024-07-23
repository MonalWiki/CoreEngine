"""
top level app for devel purposes; we need session_manager and session context to be passed/fastshippedhtml/render functitons 
"""
import os
import logging
if os:
    try:
        os.remove("launcher.log")
    except:
        pass

import sys
if sys:
    FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
    logging.basicConfig(filename="launcher.log",
                        level=logging.DEBUG, format=FORMAT)


    

from .frontend import view_function
from starlette.testclient import TestClient



from io import BytesIO
import os

from .wikicfg import NAMESPACES, WIKINAME, BACKEND_DATADIR_BASE
from .data.storage_routing import storage_routing

from .constant_keys import NAME, NAMESPACE
from .data import indexes, get_storage_revision

from .data import indexes

def startup_func():
    print ("startup func called")
    storage_base_dir = f"{BACKEND_DATADIR_BASE}/{WIKINAME}"
    storage_routing(NAMESPACES, storage_base_dir)
    indexes(storage_base_dir)
    pass


view_function.build_app(startup_func = startup_func)
from addict import Dict
from .contenttypes import CONTENTTYPE_MARKDOWN
from .constant_keys import ITEMTYPE_DEFAULT

app = view_function.app

vf = view_function
# request = Dict()
# request.session_id = "abc"
# request.query_params._dict = Dict()
# request.query_params._dict.itemtype = ITEMTYPE_DEFAULT
# request.query_params._dict.contenttype = CONTENTTYPE_MARKDOWN
#startup_func()

# # ========================== store an entity =========================
# def store_new_wikiItem():
#     wp = vf.endpoint_wikiItem(request, item_name="TreeTree4")
#     _sm = wp.session_manager
#     _ss = _sm.stubStore
#     import ofjustpy as oj
#     #print(_ss.keys())

#     # fill in user inputs
#     comment_input_ = oj.dget(_ss, "/tlctx/body/comment_input")
#     comment_input_.target.value = "some comment value"

#     content_input_ = oj.dget(_ss, "/tlctx/body/content_input")
#     content_input_.target.value = "#ektitle\n##subtitle\npara graph etc."

#     summary_input_ = oj.dget(_ss, "/tlctx/body/summary_input")
#     summary_input_.target.value = "some summary value"

#     tags_input_ = oj.dget(_ss, "/tlctx/body/tags_input")
#     tags_input_.target.value = "some tags value"

#     # ================================ end ===============================
#     btn_stub_ = oj.dget(_ss, "/tlctx/body/submit")
#     print (btn_stub_)
#     msg = Dict()
#     msg.page = wp
#     btn_stub_.target.on_click(msg)
#     # =============================== done ===============================


# def render_existing_wikiItem():
#     wp = vf.endpoint_wikiItem(request, item_name="TreeTree4")


#render_existing_wikiItem()
# # check if item is saved in the index
# from wikicoreengine.constant_keys import NAME, NAMESPACE, NAME_EXACT, NAMESPACE_DEFAULT, CURRENT, CONTENTTYPE, REVID
# from wikicoreengine.Name import CompositeName
# fqcn = CompositeName(NAMESPACE_DEFAULT, NAME_EXACT, "TreeTree4")
# whoosh_doc = indexes.document_search(**fqcn.query_terms)
#print (whoosh_doc)
# client = TestClient(app)

# response = client.get('/Home?itemtype=default&contenttype=text%2Fcsv%3Bcharset%3Dutbf-8&template= HTTP/1.1')
#response = client.get('/Home')
