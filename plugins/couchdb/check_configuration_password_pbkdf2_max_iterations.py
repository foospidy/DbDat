from distutils.version import LooseVersion

class check_configuration_password_pbkdf2_max_iterations():
    """
    check_configuration_password_pbkdf2_max_iterations:
    
    New in version 1.6:
    max_iterations - The maximum number of iterations allowed for passwords 
    hashed by the PBKDF2 algorithm. Any user with greater iterations is forbidden.
    """
    # References:
    # http://docs.couchdb.org/en/1.6.1/config/auth.html#authentication-configuration
    # http://docs.couchdb.org/en/1.6.1/config/auth.html#couch_httpd_auth/max_iterations

    TITLE    = 'Maximum Password Hashing Iterations'
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
            if 'max_iterations' in self.db.config()['couch_httpd_auth']:
                max = self.db.config()['couch_httpd_auth']['max_iterations']
                
                if int(max) < 10000:
                    self.result['level']  = 'RED'
                    output               += 'max_iterations is (%s) low.\n' % (max)
                elif int(max) < 20000:
                    self.result['level']  = 'YELLOW'
                    output               += 'max_iterations is (%s) ok.\n' % (max)
                else:
                    self.result['level']  = 'GREEN'
                    output               += 'max_iterations is (%s) good.\n' % (max)
            else:
                self.result['level']  = 'YELLOW'
                self.result['output'] = 'max_iterations is (not found) not set.\n'
            
        else:
            self.result['level']  = 'GRAY'
            self.result['output'] = 'This check only applies to versions 1.6 and above.'
            
        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
        self.db = parent.db
