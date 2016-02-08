class check_configuration_num_db_backups():
    """
    check_configuration_num_db_backups:
    The num_db_backups parameter specifies the number of backups to retain for
    a database before the old backups is marked deleted. It is recommended that
    this parameter be set to at least 12.
    """
    # References:
    # https://benchmarks.cisecurity.org/downloads/show-single/?file=db2.120

    TITLE    = 'Backups Retention'
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
            if '(NUM_DB_BACKUPS)' in line:
                match                 = True
                value                 = line.split('=')[1].strip()
                self.result['output'] = line

                if int(value) == 0:
                    self.result['level'] = 'RED'
                if int(value) >= 12:
                    self.result['level'] = 'GREEN'
                else:
                    self.result['level'] = 'YELLOW'

        if not match:
            self.result['level']  = 'GREEN'
            self.result['output'] = 'Setting not found, default is 12.'
        
        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
