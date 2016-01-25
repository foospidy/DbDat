class check_information_database_list():
    """
    check_information_database_list:
    List of availible databases.
    """
    # References:

    TITLE    = 'Database list'
    CATEGORY = 'Information'
    TYPE     = 'nosql'
    SQL         = None # SQL not needed... because this is NoSQL.

    verbose = False
    skip    = False
    result  = {}

    db      = None

    def do_check(self):
        try:
            dblist                = self.db.database_names()
            self.result['level']  = 'GREEN'
            output                = ''

            for db in dblist:
                output += '%s\n' % (db)

        except Exception as e:
            print e
            self.result['level']  = 'ORANGE'
            output                = 'Problem accessing database list, message:\n%s\n' % (e)

        self.result['output'] = output

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
        self.db = parent.db
