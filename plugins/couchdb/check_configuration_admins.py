class check_configuration_admins():
    """
    check_configuration_admins:
    Configured CouchDB admins
    """
    # References:
    # http://guide.couchdb.org/draft/security.html
    # http://docs.couchdb.org/en/1.6.1/config/auth.html#admins

    TITLE    = 'Admins'
    CATEGORY = 'Configuration'
    TYPE     = 'nosql'
    SQL      = None  # SQL not needed... because this is NoSQL.

    verbose = False
    skip    = False
    result  = {}
    db      = None

    def do_check(self):
        admins = self.db.config()['admins']
        output = ''

        if len(admins) > 0:
            self.result['level']  = 'GREEN'
            output                = 'Configured admins:\n'

            for admin in admins:
                output += '%s\n' % (admin)
        else:
            self.result['level']  = 'RED'
            output                = 'No admins found. CouchDB Admin Party in effect.'

        self.result['output'] = output

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
        self.db = parent.db
