import partools.dq as dq
import partools.rl as rl
from partools.test import gl
from partools.test.sql import interrupt


def reqlist(inp, out, query, tr=False, md='', cnx=3, elt=200):

    rl.reqlist(
        DB=gl.SQL_DB,
        QUERY_IN=query,
        IN_PATH=inp,
        OUT_PATH=out,
        VAR_DICT={'TABLE_NAME': gl.SQL_T_TEST},
        MAX_DB_CNX=cnx,
        NB_MAX_ELT_IN_STATEMENT=elt,
        SKIP_JOIN=False,
        SKIP_SQL=False,
        CHECK_DUP=True,
        OPEN_OUT_FILE=False,
        TEST_RECOVER=tr,
        MD=md,
    )


def left_join_files(left, right, ref):
    rl.left_join_files(left, right, gl.RL_OUT_JOIN, debug=False)
    dq.file_match(ref, gl.RL_OUT_JOIN)


def reqlist_interrupted(inp, out, query, cnx):
    init_msg = "[rl] reqlist: start"
    kwargs = {"inp": inp, "out": out, "query": query, "tr": True, "cnx": cnx}
    interrupt(reqlist, kwargs, init_msg)
