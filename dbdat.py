#!/usr/bin/python

import sys
import os
import ConfigParser
import argparse
import json

# prevent creation of compiled bytecode files
sys.dont_write_bytecode = True

class dbscan():
    db      = None
    dbcurs  = None
    dbtype  = None
    dbhost  = None
    dbport  = None
    dbname  = None
    dbuser  = None
    dbpass  = None
    appuser = None
    config  = None
    checks  = None
    verbose = False
    report  = None

    def connect(self):
        try:
            if 'mysql' == self.dbtype:
                import MySQLdb

                self.db     = MySQLdb.connect(host=self.dbhost, user=self.dbuser, passwd=self.dbpass, db=self.dbname)
                self.dbcurs = self.db.cursor()

            elif 'postgresql' == self.dbtype:
                import psycopg2

                self.db     = psycopg2.connect(host=self.dbhost, user=self.dbuser, password=self.dbpass, dbname=self.dbname)
                self.dbcurs = self.db.cursor()

            elif 'oracle' == self.dbtype:
                import cx_Oracle

                self.db     = cx_Oracle.connect(self.dbuser + '/' + self.dbpass + '@' + self.dbhost + '/' + self.dbname)
                self.dbcurs = self.db.cursor()

            elif 'mssql' == self.dbtype:
                import pymssql

                self.db     = pymssql.connect(self.dbhost, self.dbuser, self.dbpass, self.dbname)
                self.dbcurs = self.db.cursor()

            elif 'sybase' == self.dbtype:
                #TODO
                print("Sybase is not yet supported")
                quit()

            elif 'db2' == self.dbtype:
                #TODO
                print("DB2 is not yet supported")
                quit()

            elif 'mongodb' == self.dbtype:
                from pymongo import MongoClient

                self.db = MongoClient(self.dbhost, int(self.dbport))

                self.db['admin'].authenticate(self.dbuser, self.dbpass)

            elif 'couchdb' == self.dbtype:
                import couchdb
                
                self.db = couchdb.Server(self.dbhost + ':' + self.dbport)

            else:
                raise Exception('Unknown database type!')

        except Exception as e:
            print 'Error connecting to database!'
            print 'Error detail:'
            print '%s' % (str(e))
            quit()

    def disconnect(self):
        if self.verbose:
            print('Closing database connection.')

        if 'couchdb' != self.dbtype:
            self.db.close()

    def hacktheplanet(self):
        result = {}

        if self.verbose:
            import pprint
            pp = pprint.PrettyPrinter(indent=4)

        # setup report file
        with open(self.report, 'w') as report_file:
            report_file.write('{"title":"' + self.describe_scan() + '", "report_data":[')

        count = 0 # counter for reporting

        for database_check in self.checks:
            # load a database check
            check = self.load_class('plugins.' + self.dbtype + '.' + database_check)
            c     = check(self)

            if self.verbose:
                print(c.__doc__)

            # first get title, category, and description
            result['title']       = c.TITLE
            result['category']    = c.CATEGORY
            result['description'] = c.__doc__

            if 'configuration_file' == c.TYPE:
                result['result'] = c.do_check(self.config)

            elif 'nosql' == c.TYPE:
                try:
                    result['result'] = c.do_check()

                except Exception as e:
                    print(e)

            else:
                try:
                    # perform database check and get result
                    self.dbcurs.execute(c.SQL)

                    rows             =   self.dbcurs.fetchall()
                    result['result'] = c.do_check(rows)

                except Exception as e:
                    # sql execution error possible, issue rollback and capture error in results
                    if 'postgresql' == self.dbtype:
                        self.db.rollback()

                    c.result['level']  = 'ORANGE'
                    c.result['output'] = str(e)
                    result['result']   = c.result

                    if self.verbose:
                        print('\tException: %s' % str(e))

            if self.verbose:
                print('Result:')
                pp.pprint(result)

            # write result to report file
            with open(self.report, 'a') as report_file:
                comma = ''

                if count > 0:
                    comma = ','

                # dump them JSONs
                report_file.write(comma + json.dumps(result))

                count += 1

        # finalize report file
        with open(self.report, 'a') as report_file:
            report_file.write(']}')

    def describe_scan(self):
        return 'Assesment: %s database %s on %s with the user %s and %s queries.' % (self.dbtype, self.dbname, self.dbhost, self.dbuser, str(len(self.checks)))

    def load_class(self, name):
        components = name.split('.')
        module     = __import__(components[0])

        for component in components[1:]:
            module = getattr(module, component)

        return module

    def __init__(self, dbtype=None):
        self.dbtype = dbtype
        self.dbhost = 'localhost'
        self.checks = []

        # get check files for database type
        for file in os.listdir(os.path.dirname(os.path.abspath(__file__)) + '/plugins/' + self.dbtype):
            if file.startswith('check_') and file.endswith('.py'):
                self.checks.append(file[:-3])

if __name__ == "__main__":
    SUPPORTED_DB = ('mysql', 'postgresql', 'oracle', 'mssql', 'mongodb', 'couchdb')

    # parse command line arguments
    parser = argparse.ArgumentParser(description='At minimum, the -p or -l option must be specified.')

    parser.add_argument('-p', help='Specify the database profile.')
    parser.add_argument('-l', help='List all database profiles.', default=False, action='store_true')
    parser.add_argument('-v', help='Verbos output.', default=False, action='store_true')

    arguments = parser.parse_args()

    if not (arguments.l or arguments.p):
        parser.error('Either -p or -l must be provided.')

    # read configuration
    configuration      = ConfigParser.ConfigParser()
    configuration_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'etc', 'dbdat.conf')

    try:
        configuration.read(configuration_file)

        if arguments.l:
            # list all configured profiles and quit
            if 0 == len(configuration._sections):
                print('No profiles configured.')
            else:
                for section in configuration._sections:
                    print(section)

            quit()

        # get database profile and check for supported db type
        if configuration.get(arguments.p, 'database_type') not in SUPPORTED_DB:
            print 'Invalid database! Supported databases are %s' % (str(SUPPORTED_DB))
            quit()

    except ConfigParser.ParsingError as e:
        print('Error parsing configuration file.')
        quit()
    except ConfigParser.NoSectionError as e:
        print('The database profile "%s" does not exist.' % (arguments.p))
        quit()

    # initialize dbscan
    scan = dbscan(configuration.get(arguments.p, 'database_type'))

    scan.verbose = arguments.v
    scan.dbhost  = configuration.get(arguments.p, 'server')
    scan.dbport  = configuration.get(arguments.p, 'port')
    scan.dbname  = configuration.get(arguments.p, 'database')
    scan.config  = configuration.get(arguments.p, 'configuration_file')
    scan.report  = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'reports', 'data', 'report.json')  # todo - dynamic file naming

    if len(configuration.get(arguments.p, 'privileged_account')):
        scan.dbuser  = configuration.get(arguments.p, 'privileged_account')
        scan.dbpass  = configuration.get(arguments.p, 'privileged_account_password')
        scan.appuser = configuration.get(arguments.p, 'application_account')

        if scan.verbose:
            print('os: ' + sys.platform)

        print(scan.describe_scan())
        scan.connect()
        scan.hacktheplanet()
        scan.disconnect()
