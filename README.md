# DbDat
Db Database Assessment Tool

better instructions to come, but for now:

## Dependencies
MySQL support: `pip install MySQL-python`

PostgreSQL support: `pip install psycopg2`

Oracle support: `pip install cx_Oracle`

MS SQL support: `pip install pymssql`

## Running DbDat

Add a connection profile in etc/dbdat.conf

run: `python dbdat.py -p <profie name>`

to view the report cd to reports directory and run `python -m SimpleHTTPServer 9000` (or choose a port number you prefer). Then open your browser and navigate to http://localhost:9000
