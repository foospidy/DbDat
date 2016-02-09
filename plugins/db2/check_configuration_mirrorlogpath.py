class check_configuration_mirrorlogpath():
    """
    check_configuration_mirrorlogpath:
    The mirrorlogpath parameter specifies a location to store the mirror copy
    of the logs. It is recommended that this parameter be set to a secure
    location.
    """
    # References:
    # https://benchmarks.cisecurity.org/downloads/show-single/?file=db2.120

    TITLE    = 'Log Mirror Location'
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
            if '(MIRRORLOGPATH)' in line:
                value                 = line.split('=')[1].strip()
                self.result['output'] = line
                match                 = True

                if '' != value.strip():
                    self.result['level'] = 'GREEN'
                else:
                    self.result['level'] = 'RED'

        if not match:
            self.result['level']  = 'RED'
            self.result['output'] = 'Setting not found, the mirror log path should not be empty.'
        
        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
