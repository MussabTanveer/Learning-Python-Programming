# wrong relative import
from .mymodule import divide  # error
# see lib/mylib.py and lib/operations/operator.py file for relative imports

print("32-relative-imports", __name__)
