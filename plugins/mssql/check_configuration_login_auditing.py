class check_configuration_login_auditing():
    """
    check_configuration_login_auditing:
    Log both successful and failed login SQL Server authentication attempts.
    """
    # References:
    # https://benchmarks.cisecurity.org/downloads/show-single/index.cfm?file=sql2012DB.120

    TITLE    = 'Login Auditing'
    CATEGORY = 'Configuration'
    TYPE     = 'sql'
    SQL         = "xp_loginconfig 'audit level'"

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):

        for rows in results:
            for row in rows:
                if 'none' == row[1]:
                    self.result['level']  = 'RED'
                    self.result['output'] = 'Login audit logging is (%s) not enabled.' % (row[1])
                elif 'all' != row[1]:
                    self.result['level']  = 'YELLOW'
                    self.result['output'] = 'Logging of %s logins only is enabled.' % (row[1])
                else:
                    self.result['level']  = 'GREEN'
                    self.result['output'] = 'Logging of successful and failed logins enabled.'

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
