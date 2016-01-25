class check_configuration_old_passwords():
    """
    check_configuration_old_passwords:
    This configuration parameter forces use of older insecure password hashing method.
    """
    # References:
    # https://benchmarks.cisecurity.org/downloads/show-single/index.cfm?file=mysql.102

    TITLE    = 'Old Passwords'
    CATEGORY = 'Configuration'
    TYPE     = 'sql'
    SQL         = "SHOW GLOBAL VARIABLES LIKE 'old_passwords'"

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):

        for rows in results:
            for row in rows:
                if 'ON' == row[1]:
                    self.result['level']  = 'RED'
                    self.result['output'] = 'Old passwords is (%s) enabled.' % (row[1])
                else:
                    self.result['level']  = 'GREEN'
                    self.result['output'] = 'Old passwords is (%s) not enabled.' % (row[1])

            return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
