class check_information_cors_settings():
    """
    check_information_cors_settings:
    Additional CORS settings in use.
    """
    # References:
    # http://docs.couchdb.org/en/1.6.1/config/http.html#cors

    TITLE    = 'CORS Settings'
    CATEGORY = 'Information'
    TYPE     = 'nosql'
    SQL         = None # SQL not needed... because this is NoSQL.

    verbose = False
    skip    = False
    result  = {}
    db      = None

    def do_check(self):
        self.result['level']  = 'GREEN'
        output                = ''
        option                = 'credentials'
        
        if option in self.db.config()['cors']:
            value   = self.db.config()['cors'][option]
            output += '%s is set to %s\n' % (option, value)
        else:
            output += '%s is not set.\n' % (option)
        
        option = 'headers'
        
        if option in self.db.config()['cors']:
            value   = self.db.config()['cors'][option]
            output += '%s is set to %s\n' % (option, value)
        else:
            output += '%s is not set.\n' % (option)

        option = 'methods'
        
        if option in self.db.config()['cors']:
            value   = self.db.config()['cors'][option]
            output += '%s is set to %s\n' % (option, value)
        else:
            output += '%s is not set.\n' % (option)
        
        self.result['output'] = output
        
        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
        self.db = parent.db
