class check_configuration_discover():
    """
    check_configuration_discover:
    The discover parameter determines what kind of discovery requests, if any, the DB2
    serverwill fulfill.It is recommended that the DB2 server only fulfill requests from clients
    that know the given instance name.
    """
    # References:
    # https://benchmarks.cisecurity.org/downloads/show-single/?file=db2.120

    TITLE    = 'Discovery Requests'
    CATEGORY = 'Configuration'
    TYPE     = 'clp'
    SQL         = ''
    CMD      = ['db2', '-tn', 'get', 'database', 'manager', 'configuration']

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):
        for line in results[0].split('\n'):
            if '(DISCOVER)' in line:
                value                 = line.split('=')[1].strip()
                self.result['output'] = line

                if 'KNOWN' == value:
                    self.result['level'] = 'GREEN'
                else:
                    self.result['level'] = 'RED'

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
