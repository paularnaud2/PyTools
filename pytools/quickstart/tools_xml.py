# This script allows you to convert a potentially big xml file into csv.

import pytools.utils.g as g
from pytools.tools import xml
from pytools.quickstart import files_dir

# Input variables
# in_path = g.dirs['IN'] + "in.xml"
in_path = f'{files_dir}xml_in.xml'
out_path = g.dirs['OUT'] + "out.csv"

xml.parse_xml(in_path, out_path)
