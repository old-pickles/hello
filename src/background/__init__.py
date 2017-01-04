# TODO: move this "get_all_modules" function to a util

import glob
from os.path import dirname, basename, isfile

def get_all_modules():
  """
  Use to automatically import all sub-modules:
  __all__ = get_all_modules()
  """
  modules = glob.glob(dirname(__file__) + "/*.py")
  return [basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]














__all__ = get_all_modules()
