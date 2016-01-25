class check_configuration_authentication_mechanism():
    """
    check_configuration_authentication_mechanism:
    DB2 supports a number of authentication mechanisms. It is recommended that the
    DATA_ENCRYPT authentication mechanism be used.
    """
    # References:
    # https://benchmarks.cisecurity.org/downloads/show-single/?file=db2.120

    TITLE    = 'Authentication Mechanism'
    CATEGORY = 'Configuration'
    TYPE     = 'clp'
    SQL         = ''
    CMD      = ['db2', '-tn', 'get', 'database', 'manager', 'configuration']

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):
        for line in results[0].split('\n'):
            if '(AUTHENTICATION)' in line:
                value                 = line.split('=')[1].strip()
                self.result['output'] = line

                if 'DATA_ENCRYPT' == value:
                    self.result['level'] = 'GREEN'
                else:
                    self.result['level'] = 'RED'

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
