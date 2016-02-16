class check_configuration_fed_noauth():
    """
    check_configuration_fed_noauth:
    The fed_noauth parameter determines whether federated authentication will be bypassed
    at the instance. It is recommended that this parameter be set to no.

    """
    # References:
    # https://benchmarks.cisecurity.org/downloads/show-single/?file=db2.120

    TITLE    = 'Federated Authentication'
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
            if '(FED_NOAUTH)' in line:
                value                 = line.split('=')[1].strip()
                self.result['output'] = line
                match                 = True

                if 'NO' == value:
                    self.result['level'] = 'GREEN'
                else:
                    self.result['level'] = 'RED'

        if not match:
            self.result['level']  = 'GREEN'
            self.result['output'] = 'Setting not found, default value is NO.'
            
        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
