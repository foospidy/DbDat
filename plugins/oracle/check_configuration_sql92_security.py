class check_configuration_sql92_security():
    """
    check_configuration_sql92_security:
    The sql92_security parameter setting FALSE allows to grant only UPDATE or
    DELETE privileges without the need to grant SELECT privileges.
    """
    # References:
    # https://benchmarks.cisecurity.org/downloads/show-single/?file=oracle11gR2.210

    TITLE    = 'SQL92 Security'
    CATEGORY = 'Configuration'
    TYPE     = 'sql'
    SQL         = "SELECT UPPER(value) FROM v$parameter WHERE UPPER(name)='SQL92_SECURITY'"

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):

        for rows in results:
            for row in rows:
                if 'FALSE' != row[0]:
                    self.result['level']  = 'YELLOW'
                    self.result['output'] = 'SQL92_SECURITY is (%s) enabled.' % (row[0])
                else:
                    self.result['level']  = 'GREEN'
                    self.result['output'] = 'SQL92_SECURITY is (%s) not enabled.' % (row[0])

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
