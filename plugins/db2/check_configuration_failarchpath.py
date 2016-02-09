class check_configuration_failarchpath():
    """
    check_configuration_failarchpath:
    The failarchpath parameter specifies the location for the archive logs if
    the primary or secondary archive destination is not available. It is 
    recommended that this parameter be set to point to a secure location.
    """
    # References:
    # https://benchmarks.cisecurity.org/downloads/show-single/?file=db2.120

    TITLE    = 'Tertiary Archive Log Location'
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
            if '(FAILARCHPATH)' in line:
                value                 = line.split('=')[1].strip()
                self.result['output'] = line
                match                 = True

                if '' != value.strip():
                    self.result['level'] = 'GREEN'
                else:
                    self.result['level'] = 'YELLOW'

        if not match:
            self.result['level']  = 'YELLOW'
            self.result['output'] = 'Setting not found, the default value is null.'
        
        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
