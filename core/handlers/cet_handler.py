import os
from pathlib import Path
from pprint import pprint


_CLEAN_REDMOD_CACHE = True
_MO2_CACHE_ROOT_DIR = Path("C:/Modding/MO2/mods/dmp_overwrite_files")


class CETHandler:
    _CET_STRUCT_DIR = Path("bin/x64/plugins/cyber_engine_tweaks")
    _MO2_CET_ROOT_DIR = _MO2_CACHE_ROOT_DIR / _CET_STRUCT_DIR
    
    def __init__(self):
        pass