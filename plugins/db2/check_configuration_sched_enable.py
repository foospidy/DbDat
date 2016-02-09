class check_configuration_sched_enable():
    """
    check_configuration_sched_enable:
    The sched_enable parameter specifies whether the DB2 Task Center utility
    is allowed to schedule and execute tasks at the administration server. It
    is recommended that this parameter be set to OFF when the Task Scheduler 
    is not in use.
    """
    # References:
    # https://benchmarks.cisecurity.org/downloads/show-single/?file=db2.120

    TITLE    = 'Task Scheduler'
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
            if '(SCHED_ENABLE)' in line:
                match                 = True
                value                 = line.split('=')[1].strip()
                self.result['output'] = line

                if 'OFF' == value:
                    self.result['level'] = 'GREEN'
                else:
                    self.result['level'] = 'YELLOW'

        if not match:
            self.result['level']  = 'GREEN'
            self.result['output'] = 'Setting not found, default value is OFF.'
        
        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
