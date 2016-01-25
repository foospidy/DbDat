class check_configuration_ssl():
    """
    check_configuration_ssl:
    If you don't use SSL your data is traveling between your CouchDB client and CouchDB
    server unencrypted and is susceptible to eavesdropping, tampering and "man in
    the middle" attacks. This is especially important if you are connecting to your
    CouchDB server over unsecure networks like the internet.
    """
    # References:
    # https://wiki.apache.org/couchdb/CORS

    TITLE    = 'Enable SSL'
    CATEGORY = 'Configuration'
    TYPE     = 'nosql'
    SQL         = None  # SQL not needed... because this is NoSQL.

    verbose = False
    skip    = False
    result  = {}
    db      = None

    def do_check(self):
        daemons = self.db.config()['daemons']
        match   = False

        for daemon in daemons:
            if 'httpsd' == daemon:
                match = True

        if False == match:
            self.result['level']  = 'RED'
            self.result['output'] = 'SSL is not enabled.'
        else:
            self.result['level']  = 'GREEN'
            self.result['output'] = 'SSL is enabled.'

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
        self.db = parent.db
