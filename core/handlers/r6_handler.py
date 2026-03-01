import os
from pathlib import Path
from pprint import pprint


_CLEAN_REDMOD_CACHE = True
_MO2_CACHE_ROOT_DIR = Path("C:/Modding/MO2/mods/dmp_overwrite_files")


class R6Handler:
    _R6_STRUCT_DIR = Path("r6")
    _MO2_R6_ROOT_DIR = _MO2_CACHE_ROOT_DIR / _R6_STRUCT_DIR
    
    def __init__(self):
        self.rmod_cache_dir = R6Handler._MO2_R6_ROOT_DIR / Path("cache/modded")
        pass
    
    def clean_cache_dir(self):
        print("REDMod cache dir: " + str(self.rmod_cache_dir))
        print("Files to delete:")
        pprint(os.listdir(self.rmod_cache_dir))
