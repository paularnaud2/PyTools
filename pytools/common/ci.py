from os.path import exists

if not exists('pytools/_conf_main.py'):
    s = ("the PyTools package havn't been properly installed."
         " Please run one of the following commands:\n"
         "pip install -e .\n"
         "pip install .")
    raise Exception(s)
