# DbDat
Db Database Assessment Tool

better instructions to come, but for now:

## Dependencies
MySQLdb
psycopg2
cx_Oracle
pymssql

## Running DbDat

Add a connection profile in etc/dbdat.conf

run: `python dbdat.py -p <profie name>`

to view the report cd to reports directory and run `python -m SimpleHTTPServer 9000` (or choose a port number you prefer)
