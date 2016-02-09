class check_configuration_dasadm_group():
    """
    check_configuration_dasadm_group:
    The dasadm_group parameter defines the group name with DAS Administration
    (DASADM) authority for the DAS. It is recommended thatthe dasadm_group 
    group contains authorized users only.
    """
    # References:
    # https://benchmarks.cisecurity.org/downloads/show-single/?file=db2.120

    TITLE    = 'DAS Administration'
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
            if '(DASADM_GROUP)' in line:
                match                 = True
                value                 = line.split('=')[1].strip()
                self.result['output'] = line

                if '' != value.strip():
                    self.result['level'] = 'GREEN'
                else:
                    self.result['level'] = 'YELLOW'

        if not match:
            self.result['level']  = 'YELLOW'
            self.result['output'] = 'Setting not found, default value is null.'
        
        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
