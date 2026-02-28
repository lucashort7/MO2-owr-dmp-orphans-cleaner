import os
from pprint import pprint

from pathlib import Path


_CLEAN_REDMOD_CACHE = True
_MO2_CACHE_ROOT_DIR = Path("C:/Modding/MO2/mods/Cache, DB, JSON, INI and Log Files")


def _fast_scandir(dirname):
    subfolders = [Path(f) for f in os.scandir(dirname) if f.is_dir()]
    for dirname in list(subfolders):
        subfolders.extend(_fast_scandir(dirname))
    return subfolders


class CETHandler:
    _CET_STRUCT_DIR = Path("bin/x64/plugins/cyber_engine_tweaks")
    _MO2_CET_ROOT_DIR = _MO2_CACHE_ROOT_DIR / _CET_STRUCT_DIR
    
    def __init__(self):
        pass
    
    
class RED4EXTHandler:
    _RED4EXT_STRUCT_DIR = Path("red4ext")
    _MO2_RED4EXT_ROOT_DIR = _MO2_CACHE_ROOT_DIR / _RED4EXT_STRUCT_DIR
    
    def __init__(self):
        pass
    
    
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




# file_path = os.path(_MO2_CACHE_FILE_PATH)
# subfolders = fast_scandir(_MO2_CACHE_FILE_PATH)
# pprint(subfolders)

R6Handler().clean_cache_dir()




# TODO: clean REDmod cache
# TODO: clean orphans
    # TODO: or only that have new files: like config, db, etc
    