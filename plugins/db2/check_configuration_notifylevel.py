class check_configuration_notifylevel():
    """
    check_configuration_notifylevel:
    The notifylevel parameter specifies the type of administration notification
    messages that are written to the administration notification log. It is 
    recommended that this parameter be set to 3. A setting of 3 will log all fatal 
    errors, failing services, system integrity, as well as system health.
    """
    # References:
    # https://benchmarks.cisecurity.org/downloads/show-single/?file=db2.120

    TITLE    = 'Administrative Notification level'
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
            if '(NOTIFYLEVEL)' in line:
                value                 = line.split('=')[1].strip()
                self.result['output'] = line
                match                 = True

                if int(value) >= 3:
                    self.result['level'] = 'GREEN'
                elif int(value) > 0:
                    self.result['level'] = 'YELLOW'
                else:
                    self.result['level'] = 'RED'

        if not match:
            self.result['level']  = 'GREEN'
            self.result['output'] = 'Setting not found, default value is 3.'
        
        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
