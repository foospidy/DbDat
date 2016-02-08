class check_configuration_autorestart():
    """
    check_configuration_autorestart:
    The autorestart parameter specifies if the database instance should restart
    after an abnormal termination. It is recommended that this parameter be set
    to ON.
    """
    # References:
    # https://benchmarks.cisecurity.org/downloads/show-single/?file=db2.120

    TITLE    = 'Auto Restart'
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
            if '(AUTORESTART)' in line:
                value                 = line.split('=')[1].strip()
                self.result['output'] = line
                match                 = True

                if 'ON' == value:
                    self.result['level'] = 'GREEN'
                else:
                    self.result['level'] = 'RED'

        if not match:
            self.result['level']  = 'GREEN'
            self.result['output'] = 'Setting not found, default is ON.'
        
        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
