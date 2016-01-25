class check_configuration_allow_jsonp():
    """
    check_configuration_allow_jsonp:
    JSONP (JSON with Padding) is a technique used by web developers to overcome
    the cross-domain restrictions imposed by browsers to allow data to be
    retrieved from systems other than the one the page was served by.
    """
    # References:

    TITLE    = 'Allow JSONP'
    CATEGORY = 'Configuration'
    TYPE     = 'nosql'
    SQL         = None # SQL not needed... because this is NoSQL.

    verbose = False
    skip    = False
    result  = {}
    db      = None

    def do_check(self):
        value = self.db.config()['httpd']['allow_jsonp']

        if 'false' == value:
            self.result['level']  = 'GREEN'
            self.result['output'] = 'JSONP is (%s) not enabled.' % (value)
        else:
            self.result['level']  = 'RED'
            self.result['output'] = 'JSONP is (%s) enabled.' % (value)

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
        self.db = parent.db
