from distutils.version import LooseVersion

class check_information_public_fields():
    """
    check_information_public_fields:
    A comma-separated list of field names in user documents 
    (in couch_httpd_auth/authentication_db) that can be read by any user. 
    If unset or not specified, authenticated users can only retrieve their 
    own document.
    """
    # References:
    # http://docs.couchdb.org/en/1.6.1/config/auth.html#couch_httpd_auth/public_fields

    TITLE    = 'Public Fields'
    CATEGORY = 'Information'
    TYPE     = 'nosql'
    SQL         = None # SQL not needed... because this is NoSQL.

    verbose = False
    skip    = False
    result  = {}
    db      = None

    def do_check(self):
        version_number = self.db.version()
        
        if LooseVersion(version_number) >= LooseVersion("1.4"):
            self.result['level']  = 'GREEN'
            self.result['output'] = 'No fields specified as public_fields.'
            
            if 'public_fields' in self.db.config()['couch_httpd_auth']:
                value                 = self.db.config()['couch_httpd_auth']['public_fields']
                self.result['output'] = value

        else:
            self.result['level']  = 'GRAY'
            self.result['output'] = 'This check only applies to versions 1.4 and above.'
        
        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
        self.db = parent.db
