class check_configuration_ssl_verify_cert():
    """
    check_configuration_ssl_verify_cert:
    Set to true to validate peer certificates.
    """
    # References:
    # http://docs.couchdb.org/en/1.6.1/config/http.html#ssl/verify_ssl_certificates

    TITLE    = 'Verify SSL Certificates'
    CATEGORY = 'Configuration'
    TYPE     = 'nosql'
    SQL         = None  # SQL not needed... because this is NoSQL.

    verbose = False
    skip    = False
    result  = {}
    db      = None

    def do_check(self):
        option = 'verify_ssl_certificates'
        value  = self.db.config()['ssl'][option]

        if 'false' == value:
            self.result['level']  = 'RED'
            self.result['output'] = '%s is (%s) not enabled.' % (option, value)
        else:
            self.result['level']  = 'GREEN'
            self.result['output'] = '%s is (%s) enabled.' % (option, value)

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
        self.db = parent.db
