import os
import pytools.common as com
from . import gl


def restart():

    file_list = com.get_file_list(gl.TMP_PATH)
    a = len(file_list)
    if a == 0:
        return

    s = "Work in progress detected. Kill? (y/n)"
    if gl.TEST_RESTART:
        com.log(s)
        com.log_print("n (TEST_RESTART = True)")
    elif com.log_input(s) == 'y':
        com.mkdirs(gl.TMP_PATH, True)
        return

    modify_ql(file_list)
    com.log("Query list modified according previous work in progress. "
            f"Restarting from query '{gl.QUERY_LIST[0][1]}'")


def modify_ql(file_list):
    # Modifies the query list by deleting element already
    # in file list. EC files are also deleted.

    list_out = []
    for elt in gl.QUERY_LIST:
        comp_elt = elt[1] + gl.FILE_TYPE
        comp_elt_ec = elt[1] + gl.EC + gl.FILE_TYPE
        if comp_elt not in file_list:
            list_out.append(elt)
        if comp_elt_ec in file_list:
            ec_path = gl.TMP_PATH + comp_elt_ec
            os.remove(ec_path)
            com.log(f"EC file {ec_path} deleted")

    gl.QUERY_LIST = list_out
