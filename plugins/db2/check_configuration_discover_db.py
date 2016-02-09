class check_configuration_discover_db():
    """
    check_configuration_discover_db:
    The discover_db parameter specifies if the database will respond to a discovery
    request from a client. It is recommended that this parameter be set to DISABLE.
    """
    # References:
    # https://benchmarks.cisecurity.org/downloads/show-single/?file=db2.120

    TITLE    = 'Database Discovery'
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
            if '(DISCOVER_DB)' in line:
                value                 = line.split('=')[1].strip()
                self.result['output'] = line
                match                 = True

                if 'DISABLE' == value:
                    self.result['level'] = 'GREEN'
                else:
                    self.result['level'] = 'RED'
        
        if not match:
            self.result['level']  = 'RED'
            self.result['output'] = 'Setting not found, the default is ENABLED.'
        
        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
