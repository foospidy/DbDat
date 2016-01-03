# DbDat
**Db Database Assessment Tool**

DbDat performs numerous checks on a database to evaluate security. The categories of checks performed are configuration, privileges, users, and information. Checks are performed by running SQL queries or database reading configuration files. The goal of this tool is to highlight issues that need immediate attention and identify configuration settings that should be reviewed for appropriateness. This tool is not for identifying SQL Injection vulnerabilities in an application, there are good tools available for that already (e.g. https://github.com/sqlmapproject and https://github.com/tcstool/NoSQLMap). Rather, this tool can help you better understand the potential impact of a successful SQL Injection attack due to weak configuration or access controls. A majority of the checks are from the CIS Security Benchmarks for databases, so thanks to the CIS and the benchmark documents can be found here: https://benchmarks.cisecurity.org/downloads/browse/index.cfm?category=benchmarks.servers.database 

**Creating New Database Checks**

_Pull requests are very welcome!_ Checks are organized by database type (e.g. MySQL, Oracle, MS SQL, etc.) in the plugins folder. Each check is a single python file. When adding a new check file an import statement needs to be added to the corresponding plugin directory's `__init__.py` file. The code pattern for the checks are fairly consistent. Until I can provide more detailed documentation, review the existing files to get a sense of how they are structured. Note the difference between checks of type sql and configuration_file.

## Running DbDat

1. Be sure you have the necessary dependencies installed for Python scripts to connect to your target database. See dependencies section below.
2. Add a connection profile entry in the `etc/dbdat.conf` file for each database you want to assess.
3. Run: `python dbdat.py -p <profile name>`

To view the report cd to reports directory and run `python -m SimpleHTTPServer 9000` (or choose a port number you prefer). Then open your browser and navigate to http://localhost:9000

## Dependencies
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
- todo

#####MongoDB support
- todo
