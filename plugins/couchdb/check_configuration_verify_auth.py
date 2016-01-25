class check_configuration_verify_auth():
    """
    check_configuration_verify_auth:
    Verifying authentication is required.
    """
    # References:

    TITLE    = 'Authentication Required'
    CATEGORY = 'Configuration'
    TYPE     = 'nosql'
    SQL         = None  # SQL not needed... because this is NoSQL.

    verbose = False
    skip    = False
    result  = {}

    db      = None

    def do_check(self):
        try:
            config                = self.db.config()
            self.result['level']  = 'RED'
            self.result['output'] = 'Unauthenticated connection succeded.'

        except Exception as e:
            self.result['level']  = 'GREEN'
            self.result['output'] = 'Unauthenticated connection failed, message:\n%s\n' % (e)

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
        import couchdb
        from urlparse import urlparse

        # parent connection is authenticated so create a new unauthenticated connection
        url     = urlparse(parent.dbhost)
        self.db = couchdb.Server(url.scheme + '://' + url.hostname + ':' + parent.dbport)
