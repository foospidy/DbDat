class check_configuration_require_valid_user():
    """
    check_configuration_require_valid_user:
    When this option is set to true, no requests are allowed from anonymous users. 
    Everyone must be authenticated.
    """
    # References:
    # http://docs.couchdb.org/en/1.6.1/config/auth.html#authentication-configuration

    TITLE    = 'Require Valid User'
    CATEGORY = 'Configuration'
    TYPE     = 'nosql'
    SQL         = None # SQL not needed... because this is NoSQL.

    verbose = False
    skip    = False
    result  = {}
    db      = None

    def do_check(self):
        value  = self.db.config()['couch_httpd_auth']['require_valid_user']

        if 'false' == value:
            self.result['level']  = 'RED'
            self.result['output'] = '%s is (%s) not enabled.' % (self.TITLE, value)
        else:
            self.result['level']  = 'GREEN'
            self.result['output'] = '%s is (%s) enabled.' % (self.TITLE, value)

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
        self.db = parent.db
