class check_configuration_auto_maint():
    """
    check_configuration_auto_maint:
    Enable automatic database maintenance on your DB2 instance. It is recommended
    that the DB2 Automatic Maintenance tool be used to ensure that the instance
    is performing optimally.
    """
    # References:
    # https://benchmarks.cisecurity.org/downloads/show-single/?file=db2.120

    TITLE    = 'Database Maintenance'
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
            if '(AUTO_MAIN)' in line:
                match                 = True
                value                 = line.split('=')[1].strip()
                self.result['output'] = line

                if 'ON' == value:
                    self.result['level'] = 'GREEN'
                else:
                    self.result['level'] = 'YELLOW'

        if not match:
            self.result['level']  = 'GREEN'
            self.result['output'] = 'Setting not found, default value is ON.'
        
        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
