class check_configuration_remote_listener():
    """
    check_configuration_remote_listener:
    The    remote_listener setting determines whether or not a    valid listener can be
    established on a system separate from the database instance.
    """
    # References:
    # https://benchmarks.cisecurity.org/downloads/show-single/?file=oracle11gR2.210

    TITLE    = 'Remote Listener'
    CATEGORY = 'Configuration'
    TYPE     = 'sql'
    SQL         = "SELECT UPPER(value) FROM v$parameter WHERE UPPER(name)='REMOTE_LISTENER'"

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):
        self.result['level']  = 'GREEN'
        self.result['output'] = 'Remote Listener is not enabled.'

        for rows in results:
            for row in rows:
                if None != row[0]:
                    self.result['level']  = 'RED'
                    self.result['output'] = 'Remote Listener is (%s) enabled.' % (row[0])

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
