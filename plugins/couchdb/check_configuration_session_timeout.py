class check_configuration_session_timeout():
    """
    check_configuration_session_timeout:
    Number of seconds since the last request before sessions will be expired.
    """
    # References:
    # http://docs.couchdb.org/en/1.6.1/config/auth.html#couch_httpd_auth/timeout

    TITLE    = 'Session Timeout'
    CATEGORY = 'Configuration'
    TYPE     = 'nosql'
    SQL         = None # SQL not needed... because this is NoSQL.

    verbose = False
    skip    = False
    result  = {}
    db      = None

    def do_check(self):
        value  = self.db.config()['couch_httpd_auth']['timeout']

        if int(value) <= 600:
            self.result['level']  = 'GREEN'
            self.result['output'] = '%s is (%s) good.' % (self.TITLE, value)
        elif int(value) <= 1200:
            self.result['level']  = 'GREEN'
            self.result['output'] = '%s is (%s) ok.' % (self.TITLE, value)
        else:
            self.result['level']  = 'RED'
            self.result['output'] = '%s is (%s) high.' % (self.TITLE, value)

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
        self.db = parent.db
