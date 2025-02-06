"""
Here we add the parent directory to the sys.path so that we can import the modules from the parent directory.
"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))