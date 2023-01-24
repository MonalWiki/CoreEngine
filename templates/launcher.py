import os
import logging

if os:
    try:
        os.remove("/tmp/launcher.log")
    except:
        pass

import sys
if sys:

    FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
    logging.basicConfig(filename="/tmp/launcher.log",
                        level=logging.DEBUG, format=FORMAT)
    logger = logging.getLogger(__name__)


from view_function import endpoint_wikiItem
import ofjustpy as oj
from wikicoreengine.tools.app_launcher_utils import startup_func


app = oj.build_app(startup_func=startup_func) 
app.add_jproute("/{item_name}", endpoint_wikiItem, "endpoint_wikiItem")
    
# create view_functions

# create app

# from starlette.testclient import TestClient
# client = TestClient(app)
# response = client.get('/Home')


