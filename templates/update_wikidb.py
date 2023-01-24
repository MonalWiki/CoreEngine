import os
import logging

if os:
    try:
        os.remove("update_wikidb.log")
    except:
        pass

import sys
if sys:

    FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
    logging.basicConfig(filename="update_wikidb.log",
                        level=logging.DEBUG, format=FORMAT)
    logger = logging.getLogger(__name__)


    
from  wikicoreengine.tools.add_wikiitem_offline import add_md_item_to_wiki

from pathlib import Path
# ================== as a sanity check add home item =================

item_name = "Home"
item_content = Path(f"./{item_name}.md").read_text()
add_md_item_to_wiki(item_name, [], [], [], item_content)
