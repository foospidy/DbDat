class check_configuration_cors_origins_wildcard():
    """
    check_configuration_cors_origins_wildcard:
    List of origins separated by a comma, * means accept all.
    """
    # References:
    # http://docs.couchdb.org/en/1.6.1/config/http.html#cors/origins

    TITLE    = 'CORS Origins Wildcard'
    CATEGORY = 'Configuration'
    TYPE     = 'nosql'
    SQL         = None # SQL not needed... because this is NoSQL.

    verbose = False
    skip    = False
    result  = {}
    db      = None

    def do_check(self):
        option = 'origins'
        
        if option in self.db.config()['cors']:
            value  = self.db.config()['cors'][option]

            if '*' == value:
                self.result['level']  = 'RED'
                self.result['output'] = '%s is (%s) unconstrained.' % (option, value)
            else:
                self.result['level']  = 'GREEN'
                self.result['output'] = '%s is (%s) constrined.' % (option, value)
        
        else:
            self.result['level']  = 'GREEN'
            self.result['output'] = '%s is (not set) constrined.' % (option)

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
        self.db = parent.db
