class check_configuration_test_database():
    """
    check_configuration_test_database:
    Test databases should not exist in production.
    """
    # References:

    TITLE    = 'Test Database'
    CATEGORY = 'Configuration'
    TYPE     = 'nosql'
    SQL         = None # SQL not needed... because this is NoSQL.

    verbose = False
    skip    = False
    result  = {}

    db      = None

    def do_check(self):
        try:
            dblist = self.db.database_names()

            if 'test' in dblist:
                self.result['level']  = 'YELLOW'
                self.result['output'] = 'A "test" database was found.'
            else:
                self.result['level']  = 'GREEN'
                self.result['output'] = 'A "test" database was not found.'

        except Exception as e:
            self.result['level']  = 'ORANGE'
            self.result['output'] = 'Problem accessing database list, message:\n%s\n' % (e)

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
        self.db = parent.db
