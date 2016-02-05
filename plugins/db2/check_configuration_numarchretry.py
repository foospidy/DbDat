class check_configuration_numarchretry():
    """
    check_configuration_numarchretry:
    The numarchretry parameter determines how many times a database will try to
    archive the log file to the primary or the secondary archive destination
    before trying the failover directory. It is recommended that this parameter
    be set to 5.
    """
    # References:
    # https://benchmarks.cisecurity.org/downloads/show-single/?file=db2.120

    TITLE    = 'Number of Archive Retries'
    CATEGORY = 'Configuration'
    TYPE     = 'clp'
    SQL         = ''
    CMD      = ['db2', '-tn', 'get', 'database', 'manager', 'configuration']

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):
        match = False
        
        for line in results[0].split('\n'):
            if '(NUMARCHRETRY)' in line:
                match                 = True
                value                 = line.split('=')[1].strip()
                self.result['output'] = line

                if int(value) == 0:
                    self.result['level'] = 'RED'
                if int(value) == 5:
                    self.result['level'] = 'GREEN'
                else:
                    self.result['level'] = 'YELLOW'

        if not match:
            self.result['level']  = 'GREEN'
            self.result['output'] = 'Setting not found, default is 5.'
        
        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
