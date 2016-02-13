class check_configuration_audit_buffer():
    """
    check_configuration_audit_buffer:
    DB2 can be configured to use an audit buffer. It is recommended that the audit buffer size
    be set to at least 1000.
    """
    # References:
    # https://benchmarks.cisecurity.org/downloads/show-single/?file=db2.120

    TITLE    = 'Audit Buffer'
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
            if '(AUDIT_BUF_SZ)' in line:
                value                 = line.split('=')[1].strip()
                self.result['output'] = line

                if int(value) >= 1000:
                    self.result['level'] = 'GREEN'
                elif int(value) > 0:
                    self.result['level'] = 'YELLOW'
                else:
                    self.result['level'] = 'RED'

        if not match:
            self.result['level']  = 'RED'
            self.result['output'] = 'Setting not found, default value is 0.'
        
        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
