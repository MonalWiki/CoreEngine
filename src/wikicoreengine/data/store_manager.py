"""
experimental db store manager using sqlalchemy
"""
from addict import Dict


import os
import base64
import zlib

import os

from sqlite3 import connect, Row
from .crypto import make_uuid
from ..constant_keys import REVID, DATAID, SIZE, HASH_ALGORITHM
from .utils import serialize, deserialize
from ..wikicfg import STORAGETYPE, STORAGEARGS
from ..system_params import StorageType


def create_sqlalchemy_dbmanager():
    # initialize connection to engine
    def db_manager(**kwargs):
        """
        creates a database file and returns a tbl_storage function.
        tbl_storage manages tables within the databe 

        returns 
        """
        def get_tbl_manager(tbl_sa_model):
            def tbl_manager():
                def set_item(key, value):
                    value = base64.b64encode(value).decode()  # a str in base64 encoding
                    #  TODO: write py-sqlalchemy expression to store the value
                    pass

                def update_item(key, value):
                    #  TODO: write py-sqlalchemy expression to update  row with va

                def get_item(key):
                    #rows = list(conn.execute(f"select value from {tblname} where key=?", (key,)))
                    # if not rows:
                    #     raise KeyError(key)
                    # value = str(rows[0]['value'])  # a str in base64 encoding

                    
                    # write py-sqlalchemy expression to retrieve value from tbl_sa_model
                    value = base64.b64decode(value.encode())

                    return value 


                def drop_table():
                    #conn.execute(f'drop table {tblname}')
                    # write py-sqlalchemy code to drop the table

                

                tbl_manager.set_item = set_item
                tbl_manager.get_item = get_item
                tbl_manager.drop_table = drop_table
            tbl_manager()
            return tbl_manager
        def commit():
            print ("commit db on path = ", db_filepath)
            #conn.commit()
            #TOD0: issue commit 
        db_manager.commit = commit
        db_manager.get_tbl_manager = get_tbl_manager
    db_manager()
    return db_manager
