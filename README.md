# ParTools

## Introduction
This package contains a bunch of Python tools I have developed and used as a Support / Test Engineer.  
You can mainly use them for:

- Performing multi threaded SQL queries on an Oracle DB (__sql__)
- Performing multi threaded SQL queries on a given perimeter on an Oracle DB (__rl__)
- Comparing and sorting potentially big files (__dq__)
- Reading and searching potentially big files (__tools.bf__)
- Parsing potentially big XML files (__tools.xml__)
- Searching and removing duplicates (__tools.dup__)
- Filtering potentially big file with flexible conditions (__tools.filter__)
- Splitting potentially big files (__tools.split__)
- Extracting doc string from Python code (__tools.extract_doc__)
- Sending mails with gmail, outlook or without authentication (__mail__)
- Simple loging or loging in loops (``log`` and ``step_log``), manipulating files and strings, running shell commands, generating message box and many others (__utils__)

## Quickstart

Download code, __extract zip and run `pip install -e .` at the root.__

You'll find examples of use and descriptions of the different available packages and functions in the __partools/quickstart__ folder.
If you want to use the __cx_Oracle__ dependant packages (__sql__ and __rl__), you'll need an [Oracle instant client](https://www.oracle.com/uk/database/technologies/instant-client/downloads.html) whose directory you can set in the __conf.py__ file.

## The conf.py file

The __partools/conf.py__ file contains the __main user settings__ for the __partools__ package such as the path to the Oracle instant client (``ORACLE_CLIENT``). If needed, you can create a __PTconf.py__ file at the root that will be used instead of the native __partools/conf.py__ file. Similarly, you can also create a __PTconf_perso.py__ file at the root that will take over the two previous files described. This can be useful if you __work on a shared repository__ but still want/need to have your own local configurations.

## The global variable files gl.py and main functions inputs

Each package has a __gl.py__ file which sets its __global variables and constants__. Each of these variables can be passed to the main package function (e.g. rl.reqlist for the rl package) and if so, overwrites the value defined in the __gl.py__ file. In that respect, __constants defined in the gl.py file can be seen as default input values__.

## The utils package

The __partools__ package includes a __utils__ package which provides generic functions used by the other packages. As you may want to use some of them for your own code, I recommend you to check out the list of those functions in __partools/utils/\_\_init\_\_.py__. Here are a few examples:

- `save_list`: saves a list into a text file
- `load_txt`: loads a text file into a string or a list
- `list_files`: returns the list of the files in a folder
- `like`: behaves as the LIKE of Oracle SQL (you can match strings with wildcard character '\*'). Example: like('Hello World', 'He\*o w\*d') returns True
- `big_number`: converts a potentially big number into a lisible string. For example big_number(10000000) returns '10 000 000'.
- `get_duration_string`: outputs a string representing the time elapsed since the input ``start_time``. For example '3 minutes and 20 seconds'.
- ``run_cmd``: runs a Windows shell command (__sTools__)
- ``run_sqlplus``: connects to sqlplus as sysdba and runs a sql script (__sTools__)
- ``msg_box``: opens a message box containing the 'msg' input string (__sTools__)

### Logging with the utils package

If you want the `log` function to actually fill a log file, you have to run `init_log()` before using it, otherwise it will just print out the log info in the console.  
You can specify a ``format`` for the log timestamp which by default is ``'%H:%M:%S -'``. Here is what a default log line looks like:

    19:45:04 - This line has been generated by the partools.utils.log function

The `step_log` function allows you to log some information only when the input ``counter`` is a multiple of the input ``step`` (thus, it is used in loops). `step_log` can be useful to __track the progress of long processes__ such as reading or writing millions of lines in a file. The ``what`` input expects a description of what is being counted. It's default value is  ``'lines written'``.  
In order to correctly measure the elapsed time for the first log line, the ``step_log`` function has to be initialised by running ``init_sl_time()``.  
So for example, if you input ``step=500`` and don't input any ``what`` value, you should get something like this:

    19:45:04 - 500 lines written in 3 ms. 500 lines written in total.
    19:45:04 - 500 lines written in 2 ms. 1 000 lines written in total.
    19:45:04 - 500 lines written in 2 ms. 1 500 lines written in total.

### The PT folder

When first used, the __utils__ package gets initialised by creating a __PT__ directory (which you can set in __conf.py__). It is intended to contain the __log files and the temporary files__ generated by the different __ParTools__'s scripts. It also has __in__ and __out__ directories used by the __test__ package (and of course that you can also use for your own scripts using __ParTools__).

## Recover functionalities

``sql.download``, ``rl.reqlist`` and ``sql.execute`` have a __recovery functionality__. This means that if the process is unexpectedly stopped (e.g. because of network issues), then when relaunched, the script __automatically restarts from where it stopped__. When you run long processes (e.g. extracting millions of lines from a database), this can save you a significant amount of time if something goes wrong (especially when close to the end!).  
The reliability of these recovery mechanisms is ensured by automated tests using the ``multiprocessing`` library to simulate the unexpected process interruption.

## Running the automated tests

If you want to ensure that all __ParTools__ fonctionnalites work correctly on your environment (or if you want a bigger overview of the available functionalities than that provided in the quickstart scripts), you can __run ``pytest`` at the root__.

If you want the __cx_Oracle__ dependent tests (__sql__ and __rl__) to be working, you'll need access to an __Oracle database with read and write permissions__. If you don't have any, you can install an [Oracle XE](https://www.oracle.com/database/technologies/appdev/xe.html) local database. Once you have such a database (XE or other), you have to set it in the ``CONF_ORACLE`` variable from __conf.py__ and then set its name in the ``SQL_DB`` variable defined in __partools/test/gl.py__. If you want to bypass the tests using __cx_Oracle__, you can simply set this ``SQL_DB`` variable to ``''``  .

Happy scripting!
