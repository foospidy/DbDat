class check_configuration_srvcon_auth():
    """
    check_configuration_srvcon_auth:
    The srvcon_auth parameter specifies how and where authentication is to take
    for incoming connections to the server. It is recommended that this parameter
    is not set to CLIENT.
    
    If a value is not specified, DB2 uses the value of the authentication database
    manager configuration parameter.
    """
    # References:
    # https://benchmarks.cisecurity.org/downloads/show-single/?file=db2.120

    TITLE    = 'Server Based Authentication'
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
            if '(SRVCON_AUTH)' in line:
                value                 = line.split('=')[1].strip()
                self.result['output'] = line
                match                 = True

                if value == 'CLIENT':
                    self.result['level'] = 'RED'
                else:
                    self.result['level'] = 'GREEN'

        if not match:
            self.result['level']  = 'GREEN'
            self.result['output'] = 'Setting not found, default is NOT_SPECIFIED.\n\nIf a value is not specified, DB2 uses the value of the authentication database manager configuration parameter.'
            
        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
