# DbDat
Db Database Assessment Tool

## Dependencies
#MySQL support:

Run: `pip install MySQL-python`

Or on Debian, run: `apt-get install python-mysqldb`

#PostgreSQL support: `pip install psycopg2`

#Oracle support: `pip install cx_Oracle`
- https://cx-oracle.readthedocs.org/en/latest/index.html

#MS SQL support: `pip install pymssql`
- https://pymssql.readthedocs.org/en/latest/index.html

## Running DbDat

Add a connection profile in etc/dbdat.conf

run: `python dbdat.py -p <profie name>`

to view the report cd to reports directory and run `python -m SimpleHTTPServer 9000` (or choose a port number you prefer). Then open your browser and navigate to http://localhost:9000
