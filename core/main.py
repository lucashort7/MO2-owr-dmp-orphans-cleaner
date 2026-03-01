import os
from pathlib import Path
from pprint import pprint

from core.handlers.cet_handler import CETHandler
from core.handlers.r6_handler import R6Handler


_CLEAN_REDMOD_CACHE = True
_MO2_CACHE_ROOT_DIR = Path("C:/Modding/MO2/mods/dmp_overwrite_files")


def _fast_scandir(dirname):
    subfolders = [Path(f) for f in os.scandir(dirname) if f.is_dir()]
    for dirname in list(subfolders):
        subfolders.extend(_fast_scandir(dirname))
    return subfolders


# TODO: clean REDmod cache
R6Handler().clean_cache_dir()

# TODO: clean orphans
CETHandler()