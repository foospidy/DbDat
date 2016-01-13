# DbDat
**Db Database Assessment Tool**

DbDat performs numerous checks on a database to evaluate security. The categories of checks performed are configuration, privileges, users, and information. Checks are performed by running queries or reading database configuration files. The goal of this tool is to highlight issues that need immediate attention and identify configuration settings that should be reviewed for appropriateness. This tool is not for identifying SQL Injection vulnerabilities in an application, there are good tools available for that already (e.g. https://github.com/sqlmapproject). Also, this tool does not attempt to determine what CVEs may impact the version of the target database (but may do so in the future - maybe). Rather, this tool can help you better understand the potential impact of a successful SQL Injection attack due to weak configuration or access controls. A majority of the checks are from the CIS (https://cisecurity.org) Security Benchmarks for databases, so thanks to the CIS! The benchmark documents can be found here: https://benchmarks.cisecurity.org/downloads/browse/index.cfm?category=benchmarks.servers.database

I highly recommend downloading the benchmark document for your target database as it contains additional information about the checks performed.

Finally, DbDat is intended to be a framework to enable easy creation of new plugins and checks. Contributions from the security, or even database administrator, community is what will make this a great tool. Please contribute!

**Developing New Database Checks**

_Pull requests are very welcome!_ Checks are organized by database type (e.g. MySQL, Oracle, MS SQL, etc.) in the plugins folder. Each check is a single python file that must have `check_` at the begining of the file name. Each file contains a class with a `do_check` method. This method is the primary logic for checks. The quick way to get started is to copy an existing check file and modify it. However, see the Developing Plugins section below for more details.

## Running DbDat

1. Be sure you have the necessary dependencies installed for Python scripts to connect to your target database. See dependencies section below.
2. Add a connection profile entry in the `etc/dbdat.conf` file for each database you want to assess.
3. Run: `python dbdat.py -p <profile name>`
4. View the report. To view the report `cd` to reports directory and run `python -m SimpleHTTPServer 9000` (or choose a port number you prefer). Then open your browser and navigate to `http://localhost:9000`.

To see a list of additional command line arguments run `python dbdat.py -h`

#### Report Output

The report organizes results by levels, which are RED, YELLOW, ORANGE, GRAY, and GREEN.

- RED - items needing immediate attention.
- YELLOW - items needing review.
- ORANGE - checks that failed to execute properly.
- GRAY - items that may not be applicable to the version of the database being assessed.
- GREEN - itesm that passed

## Dependencies

So far DbDat has been tested on Debian Linux and Windows 7 with Python 2.7

#####MySQL support

Run: `pip install MySQL-python`

Or on Debian, run: `apt-get install python-mysqldb`

#####PostgreSQL support

Run: `pip install psycopg2`

#####Oracle support

Run: `pip install cx_Oracle`
- https://cx-oracle.readthedocs.org/en/latest/index.html

_Note: you will need to install Oracle client libraries for this to work._

#####MS SQL support

Run: `pip install pymssql`
- https://pymssql.readthedocs.org/en/latest/index.html

#####Sybase support
- todo

#####DB2 support

Run: `pip install ibm_db` or `easy_install ibm_db`

#####MongoDB support

Run: `pip install mongodb`

#####CouchDB support

Run: `pip install couchdb`

## Developing Plugins

### Plugin Folders

### Check Files

When adding a new check file an import statement needs to be added to the corresponding plugin directory's `__init__.py` file. The code pattern for the checks are fairly consistent. Until I can provide more detailed documentation, review the existing files to get a sense of how they are structured. Note the difference between checks of type sql and configuration_file.

## Other Database Security Tools

- SQLMap - https://github.com/sqlmapproject
- NoSQLMap - https://github.com/tcstool/NoSQLMap
