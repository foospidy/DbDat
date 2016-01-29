from distutils.version import LooseVersion

class check_configuration_password_pbkdf2_min_iterations():
    """
    check_configuration_password_pbkdf2_min_iterations:
    
    New in version 1.6:
    min_iterations - The minimum number of iterations allowed for passwords
    hashed by the PBKDF2 algorithm. Any user with fewer iterations is forbidden.
    """
    # References:
    # http://docs.couchdb.org/en/1.6.1/config/auth.html#authentication-configuration
    # http://docs.couchdb.org/en/1.6.1/config/auth.html#couch_httpd_auth/min_iterations

    TITLE    = 'Minimum Password Hashing Iterations'
    CATEGORY = 'Configuration'
    TYPE     = 'nosql'
    SQL         = None # SQL not needed... because this is NoSQL.

    verbose = False
    skip    = False
    result  = {}
    db      = None

    def do_check(self):
        version_number = self.db.version()
            
        if LooseVersion(version_number) >= LooseVersion("1.6"):
            if 'min_iterations' in self.db.config()['couch_httpd_auth']:
                min = self.db.config()['couch_httpd_auth']['min_iterations']
                
                if int(min) < 5000:
                    self.result['level']  = 'RED'
                    self.result['output'] = 'min_iterations is (%s) low.\n' % (min)
                elif int(min) < 10000:
                    self.result['level']  = 'YELLOW'
                    self.result['output'] = 'min_iterations is (%s) ok.\n' % (min)
                else:
                    self.result['level']  = 'GREEN'
                    self.result['output'] = 'min_iterations is (%s) good.\n' % (min)
            else:
                self.result['level']  = 'YELLOW'
                self.result['output'] = 'min_iterations is (not found) not set.\n'

        else:
            self.result['level']  = 'GRAY'
            self.result['output'] = 'This check only applies to versions 1.6 and above.'
            
        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
        self.db = parent.db
