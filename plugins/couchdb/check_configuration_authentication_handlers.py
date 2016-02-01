from distutils.version import LooseVersion
from string import whitespace

class check_configuration_authentication_handlers():
    """
    check_configuration_authentication_handlers:
    For each HTTP request that CouchDB receives, one or more authentication
    handlers are invoked to authenticate the user.
    """
    # References:
    # http://docs.couchdb.org/en/1.6.1/config/http.html#httpd/authentication_handlers
    # https://wiki.apache.org/couchdb/Security_Features_Overview#Authentication

    TITLE    = 'Authentication Handlers'
    CATEGORY = 'Configuration'
    TYPE     = 'nosql'
    SQL         = None # SQL not needed... because this is NoSQL.

    verbose = False
    skip    = False
    result  = {}
    db      = None

    def do_check(self):
        self.result['level'] = 'GREEN'
        version_number       = self.db.version()
        output               = ''
        null_handler         = False
        # list of default handlers; must not contain spaces or curly brackets
        default_handlers     = [
            'couch_httpd_oauth,oauth_authentication_handler',
            'couch_httpd_auth,cookie_authentication_handler',
            'couch_httpd_auth,default_authentication_handler'
            ]
        
        if LooseVersion(version_number) >= LooseVersion("0.11"):
            # retrieve and parse handlers
            handlers = str(self.db.config()['httpd']['authentication_handlers']).replace('{', '', 1).translate(None, whitespace).translate(None, '}').split(',{')
            
            for handler in handlers:
                if handler in default_handlers:
                    output += '%s\n' % (handler)
                elif 'couch_httpd_auth,proxy_authentication_handler' == handler:
                    self.result['level'] = 'YELLOW'
                    output += '%s - Proxy authentication handler configuration should be reviewed.\n' % (handler)
                elif 'couch_httpd_auth,null_authentication_handler' == handler:
                    null_handler = True
                    output += '%s - This enables the CouchDB admin party and should never be used!\n' % (handler)
                else:
                    self.result['level'] = 'YELLOW'
                    unknown_handler = True
                    output += '%s - Third-party authentication handlers should be reviewed.\n' % (handler)
            
            if null_handler:
                self.result['level'] = 'RED'
        else:
            self.result['level']  = 'GRAY'
            self.result['output'] = 'This check only applies to versions 0.11 and above.'
        
        self.result['output'] = output
        
        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
        self.db = parent.db
