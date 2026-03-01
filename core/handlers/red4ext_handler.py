import os
from pathlib import Path
from pprint import pprint


_CLEAN_REDMOD_CACHE = True
_MO2_CACHE_ROOT_DIR = Path("C:/Modding/MO2/mods/dmp_overwrite_files")


class RED4EXTHandler:
    _RED4EXT_STRUCT_DIR = Path("red4ext")
    _MO2_RED4EXT_ROOT_DIR = _MO2_CACHE_ROOT_DIR / _RED4EXT_STRUCT_DIR
    
    def __init__(self):
        pass