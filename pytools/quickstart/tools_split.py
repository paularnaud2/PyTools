"""
This script allows you to split a file into multiple files (e.g. if it is too
big to be opened with an app such as Excel). see in pytools/tools/gl for other
parameters.
"""

import pytools.utils.g as g
from pytools.tools import split
from pytools.quickstart import files_dir

# Input variables default values
# in_path = g.dirs['IN'] + "in.csv"
in_path = f'{files_dir}in.csv'
out_dir = g.dirs['OUT']

split.split_file(in_path, out_dir, MAX_LINE=1000)
