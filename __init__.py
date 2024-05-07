"""
Forwards the contents of ./bsz-nodes/ for reading when the whole repo is cloned into ComfyUI's /custom_nodes/ folder

Should make it compatible with https://github.com/ltdrdata/ComfyUI-Manager
"""

from importlib import machinery as ilm
from importlib import util as ilu

finder = ilm.PathFinder()
spec = finder.find_spec("bsz-nodes", __path__)
mod = ilu.module_from_spec(spec)
spec.loader.exec_module(mod)

NODE_CLASS_MAPPINGS = mod.NODE_CLASS_MAPPINGS
NODE_DISPLAY_NAME_MAPPINGS = mod.NODE_DISPLAY_NAME_MAPPINGS
