class check_information_all_dbs():
    """
    check_information_all_dbs:
    List of databases
    """
    # References:
    # http://guide.couchdb.org/draft/security.html

    TITLE    = 'All Databases'
    CATEGORY = 'Information'
    TYPE     = 'nosql'
    SQL         = None  # SQL not needed... because this is NoSQL.

    verbose = False
    skip    = False
    result  = {}
    db      = None

    def do_check(self):
        self.result['level'] = 'GREEN'
        output               = ''
        
        for database in self.db:
            output += '%s\n' % database  

        self.result['output'] = output
        
        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
        self.db = parent.db
