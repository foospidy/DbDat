# DbDat
Db Database Assessment Tool

DbDat performs numerous checks on a database to evaluate security. The categories of checks performed are configuration, privileges, users, and information. Checks are performed by running SQL queries or database reading configuration files. The goal of this tool is to highlight issues that need immediate attention and identify configuration settings that should be reviewed for appropriateness. This tool is not for identifying SQL Injection vulnerabilities in an application, there are good tools available for that already (e.g. https://github.com/sqlmapproject and https://github.com/tcstool/NoSQLMap). Rather, this tool can help you better understand the potential impact of a successful SQL Injection attack due to weak configuration or access controls. A majority of the checks are from the CIS Security Benchmarks for databases, so thanks to the CIS and the benchmark documents can be found here: https://benchmarks.cisecurity.org/downloads/browse/index.cfm?category=benchmarks.servers.database 

## Dependencies
#####MySQL support

Run: `pip install MySQL-python`

Or on Debian, run: `apt-get install python-mysqldb`

#####PostgreSQL support

Run: `pip install psycopg2`

#####Oracle support

Run: `pip install cx_Oracle`
- https://cx-oracle.readthedocs.org/en/latest/index.html

#####MS SQL support

Run: `pip install pymssql`
- https://pymssql.readthedocs.org/en/latest/index.html

#####Sybase support
- todo

#####DB2 support
- todo

#####MongoDB support
- todo

## Running DbDat

Add a connection profile in etc/dbdat.conf

run: `python dbdat.py -p <profie name>`

To view the report cd to reports directory and run `python -m SimpleHTTPServer 9000` (or choose a port number you prefer). Then open your browser and navigate to http://localhost:9000
