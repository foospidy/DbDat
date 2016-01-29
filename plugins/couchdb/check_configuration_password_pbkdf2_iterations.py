from distutils.version import LooseVersion

class check_configuration_password_pbkdf2_iterations():
    """
    check_configuration_password_pbkdf2_iterations:
    
    New in version 1.3:
    iterations - The number of iterations for password hashing by the PBKDF2 
    algorithm. A higher number provides better hash durability, but comes at
    a cost in performance for each request that requires authentication.
    
    New in version 1.6:
    min_iterations - The minimum number of iterations allowed for passwords
    hashed by the PBKDF2 algorithm. Any user with fewer iterations is forbidden.
    
    max_iterations - The maximum number of iterations allowed for passwords 
    hashed by the PBKDF2 algorithm. Any user with greater iterations is forbidden.
    """
    # References:
    # http://docs.couchdb.org/en/1.6.1/config/auth.html#authentication-configuration
    # http://docs.couchdb.org/en/1.6.1/config/auth.html#couch_httpd_auth/iterations
    # http://docs.couchdb.org/en/1.6.1/config/auth.html#couch_httpd_auth/min_iterations
    # http://docs.couchdb.org/en/1.6.1/config/auth.html#couch_httpd_auth/max_iterations

    TITLE    = 'Password Hashing Iterations'
    CATEGORY = 'Configuration'
    TYPE     = 'nosql'
    SQL         = None # SQL not needed... because this is NoSQL.

    verbose = False
    skip    = False
    result  = {}
    db      = None

    def do_check(self):
        version_number = self.db.version()
        
        if LooseVersion(version_number) >= LooseVersion("1.3"):
            value  = self.db.config()['couch_httpd_auth']['iterations']
            output = ''
            
            if int(value) < 5000:
                self.result['level']  = 'RED'
                output               += 'iterations is (%s) low.\n' % (value)
            elif int(value) < 10000:
                self.result['level']  = 'YELLOW'
                output               += 'iterations is (%s) ok.\n' % (value)
            else:
                self.result['level']  = 'GREEN'
                output               += 'iterations is (%s) good.\n' % (value)
            
            if LooseVersion(version_number) >= LooseVersion("1.6"):
                if 'min_iterations' in self.db.config()['couch_httpd_auth']:
                    min = self.db.config()['couch_httpd_auth']['min_iterations']
                    
                    if int(min) < 5000:
                        self.result['level']  = 'RED'
                        output               += 'min_iterations is (%s) low.\n' % (min)
                    elif int(min) < 10000:
                        self.result['level']  = 'YELLOW'
                        output               += 'min_iterations is (%s) ok.\n' % (min)
                    else:
                        self.result['level']  = 'GREEN'
                        output               += 'min_iterations is (%s) good.\n' % (min)

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
            
            self.result['output'] = output
        else:
            self.result['level']  = 'GRAY'
            self.result['output'] = 'This check only applies to versions 1.3 and above.'
            
        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
        self.db = parent.db
