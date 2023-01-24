"""
using meta and content create a whoosh doc
"""

from io import BytesIO
import os
from wikicoreengine.constant_keys import NAME, NAMESPACE, NAME_EXACT, NAMESPACE_DEFAULT, CURRENT, CONTENTTYPE, REVID
from wikicoreengine.constant_keys import LATEST_REVS, ALL_REVS, NAMESPACE, NAME, CONTENTTYPE, MTIME, PTIME, NAME_EXACT, WIKINAME, CONTENT, BACKENDNAME, CONTENTNGRAM, SUMMARYNGRAM, TAGS, HAS_TAG, ACTION_SAVE, UFIELDS, NAMESPACE, NAME, UFIELDS_TYPELIST, ITEMID, SUMMARY, NAMENGRAM, NAMES, NAME_SORT, CURRENT, REVID, SIZE, COMMENT, REV_NUMBER, PARENTID, REVID


from wikicoreengine.wikicfg import NAMESPACES, WIKINAME, BACKEND_DATADIR_BASE
from wikicoreengine.data.storage_routing import storage_routing
from wikicoreengine.data.indexes import indexes, storageItem_to_whooshDoc


from wikicoreengine.Name import CompositeName
from wikicoreengine.item import WikiItem


from wikicoreengine.data.IndexSchema import all_revisions_schema, latest_revisions_schema

# ====================== init db and index store =====================
storage_base_dir = f"{BACKEND_DATADIR_BASE}/{WIKINAME}"
storage_routing(NAMESPACES, storage_base_dir)
indexes(storage_base_dir)

# ================================ end ===============================

# =================== create dummy meta and content ==================
meta =  {'itemtype': 'default',
         'contenttype': 'text/x-markdown;charset=utf-8',
         'namespace': NAMESPACE_DEFAULT,
         'summary': 'some sort of summary',
         'name': ['Home3'],
         'tags': ['sfsd sfsfh tha3'],
         'comment': 'mycomment9',
         'rev_number': 1
         
         }
revid = 54892320
meta[REVID] = revid
data = b"# Hello\n## HELLOHELLO"
content = indexes.indexible_content(meta, data)
print("indexible content = ", content)
SCHEMAS = {ALL_REVS : all_revisions_schema,
           LATEST_REVS: latest_revisions_schema
    }

doc = storageItem_to_whooshDoc(meta, content, SCHEMAS[ALL_REVS], WIKINAME, 'default')
print (doc)
