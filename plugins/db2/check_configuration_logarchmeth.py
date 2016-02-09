class check_configuration_logarchmeth():
    """
    check_configuration_logarchmeth:
    The logarchmeth1 parameter specifies the type of media used for the primary
    destination of archived logs. It is recommended that this parameter be set
    to a secure location.
    """
    # References:
    # https://benchmarks.cisecurity.org/downloads/show-single/?file=db2.120

    TITLE    = 'Archive Log Location'
    CATEGORY = 'Configuration'
    TYPE     = 'clp'
    SQL         = ''
    CMD      = ['db2', '-tn', 'get', 'database', 'manager', 'configuration']

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):
        output = ''
        
        # check first destination
        match  = False
        
        for line in results[0].split('\n'):
            if '(LOGARCHMETH1)' in line:
                value                 = line.split('=')[1].strip()
                self.result['output'] = line
                match                 = True

                if '' != value.strip():
                    self.result['level'] = 'GREEN'
                else:
                    self.result['level'] = 'YELLOW'

        if not match:
            self.result['level']  = 'YELLOW'
            output               += 'LOGARCHMETH1 not found, default value is OFF.\n'
        
        # check secondary destination
        match = False
        
        for line in results[0].split('\n'):
            if '(LOGARCHMETH2)' in line:
                value                 = line.split('=')[1].strip()
                self.result['output'] = line
                match                 = True

                if '' == value.strip():
                    self.result['level'] = 'YELLOW'

        if not match:
            self.result['level']  = 'YELLOW'
            output               += 'LOGARCHMETH2 not found, default value is OFF.'
        
        self.result['output'] = output
        
        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
