class check_configuration_archretrydelay():
    """
    check_configuration_archretrydelay:
    The archretrydelay parameter specifies the number of seconds the DB2 service
    will wait before it reattempts to archive log files after a failure. It is 
    recommended that this parameter be set to 20.
    """
    # References:
    # https://benchmarks.cisecurity.org/downloads/show-single/?file=db2.120

    TITLE    = 'Archive Retry Delay'
    CATEGORY = 'Configuration'
    TYPE     = 'clp'
    SQL         = ''
    CMD      = ['db2', '-tn', 'get', 'database', 'manager', 'configuration']

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):
        enabled = True
        match   = False
        
        # first check for NUMARCHRETRY, if this value
        # is 0, then ARCHRETRYDELAY is not enabled.
        for line in results[0].split('\n'):
            if '(NUMARCHRETRY)' in line:
                value                 = line.split('=')[1].strip()

                if int(value) == 0:
                    self.result['level']  = 'RED'
                    self.result['output'] = 'Archive Retry Delay is not enabled since NUMARCHRETRY is set to 0.'
                    enabled = False
        
        if enabled:
            for line in results[0].split('\n'):
                if '(ARCHRETRYDELAY)' in line:
                    match                 = True
                    value                 = line.split('=')[1].strip()
                    self.result['output'] = line

                    if int(value) == 0:
                        self.result['level'] = 'RED'
                    if int(value) == 20:
                        self.result['level'] = 'GREEN'
                    else:
                        self.result['level'] = 'YELLOW'

            if not match:
                self.result['level']  = 'YELLOW'
                self.result['output'] = 'Setting not found, default is 20.'
        
        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
