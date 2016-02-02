class check_configuration_authentication_db():
    """
    check_configuration_authentication_db:
    Specifies the name of the system database for storing CouchDB users.
    """
    # References:
    # http://docs.couchdb.org/en/1.6.1/config/auth.html#couch_httpd_auth/authentication_db

    TITLE    = 'Authentication DB'
    CATEGORY = 'Configuration'
    TYPE     = 'nosql'
    SQL         = None # SQL not needed... because this is NoSQL.

    verbose = False
    skip    = False
    result  = {}
    db      = None

    def do_check(self):
        option = 'authentication_db'
        value  = self.db.config()['couch_httpd_auth'][option]

        if '_users' == value:
            self.result['level']  = 'GREEN'
            self.result['output'] = '%s is (%s) the standard users database.' % (option, value)
        else:
            self.result['level']  = 'YELLOW'
            self.result['output'] = '%s is (%s) a non-standard users database.' % (option, value)

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
        self.db = parent.db
