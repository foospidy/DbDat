class check_configuration_safe_show_database():
    """
    check_configuration_safe_show_database:
    This option causes the SHOW DATABASES statement to display names of only
    those databases for which the user has some kind of privilege (default in 5.1)
    """
    # References:
    # https://benchmarks.cisecurity.org/downloads/show-single/index.cfm?file=mysql.102

    TITLE    = 'Safe Show Database'
    CATEGORY = 'Configuration'
    TYPE     = 'sql'
    SQL         = "SHOW GLOBAL VARIABLES LIKE 'safe_show_database'"

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):

        for rows in results:
            for row in rows:
                if 'ON' != row[1]:
                    self.result['level']  = 'RED'
                    self.result['output'] = 'Safe Show Database is (%s) not enabled.' % (row[1])
                else:
                    self.result['level']  = 'GREEN'
                    self.result['output'] = 'Safe Show Database is (%s) enabled.' % (row[1])

            return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
