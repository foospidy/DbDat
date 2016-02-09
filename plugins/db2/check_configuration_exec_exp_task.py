class check_configuration_exec_exp_task():
    """
    check_configuration_exec_exp_task:
    The exec_exp_task parameter controls whether the DB2 Scheduler will initialize
    past tasks that were scheduled but not yet executed. It is recommended that 
    this parameter be set to NO.
    """
    # References:
    # https://benchmarks.cisecurity.org/downloads/show-single/?file=db2.120

    TITLE    = 'Execute Expired Tasks'
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
            if '(EXEC_EXP_TASK)' in line:
                match                 = True
                value                 = line.split('=')[1].strip()
                self.result['output'] = line

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
