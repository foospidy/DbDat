from distutils.version import LooseVersion

class check_configuration_users_db_public():
    """
    check_configuration_users_db_public:
    Allow all users to view user documents. By default, only admins may browse 
    all users documents, while users may browse only their own document.
    """
    # References:
    # http://docs.couchdb.org/en/1.6.1/config/auth.html#couch_httpd_auth/users_db_public

    TITLE    = 'Users DB Public'
    CATEGORY = 'Configuration'
    TYPE     = 'nosql'
    SQL         = None # SQL not needed... because this is NoSQL.

    verbose = False
    skip    = False
    result  = {}
    db      = None

    def do_check(self):
        version_number = self.db.version()
        
        if LooseVersion(version_number) >= LooseVersion("1.4"):
            if 'users_db_public' in self.db.config()['couch_httpd_auth']:
                value  = self.db.config()['couch_httpd_auth']['users_db_public']
            else:
                value = None

            if None == value:
                self.result['level']  = 'GREEN'
                self.result['output'] = 'users_db_public is (not found) not enabled.'
            elif 'false' == value:
                self.result['level']  = 'GREEN'
                self.result['output'] = '%s is (%s) not enabled.' % (self.TITLE, value)
            else:
                self.result['level']  = 'RED'
                self.result['output'] = '%s is (%s) enabled.' % (self.TITLE, value)
        else:
            self.result['level']  = 'GRAY'
            self.result['output'] = 'This check only applies to versions 1.4 and above.'
        
        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
        self.db = parent.db
