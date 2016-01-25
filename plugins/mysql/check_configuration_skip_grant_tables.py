class check_configuration_skip_grant_tables():
    """
    check_configuration_skip_grant_tables:
    This option causes the server not to use the privilege system at all. This
    gives anyone with access to the server unrestricted access to all databases.
    """
    # References:
    # https://benchmarks.cisecurity.org/downloads/show-single/index.cfm?file=mysql.102

    TITLE    = 'Skip Grant Tables'
    CATEGORY = 'Configuration'
    TYPE     = 'sql'
    SQL         = "SHOW GLOBAL VARIABLES LIKE 'skip_grant_tables'"

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):
        # if variable does not exist, so default green
        self.result['level']  = 'GREEN'
        self.result['output'] = 'Skip Grant Tables is not enabled.'

        for rows in results:
            for row in rows:
                if 'ON' == r[1]:
                    self.result['level']  = 'RED'
                    self.result['output'] = 'Skip Grant Tables is (%s) enabled.' % (row[1])
                else:
                    self.result['output'] = 'Skip Grant Tables is (%s) not enabled.' % (row[1])

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
