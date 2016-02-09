class check_information_db2system():
    """
    check_information_db2system:
    The db2system parameter specifies the DB2 system name that is used by users
    and database administrators to identify the DB2 server. It is recommended 
    that this parameter be set to a value that does not represent sensitive 
    aspects of the system.
    """
    # References:
    # https://benchmarks.cisecurity.org/downloads/show-single/?file=db2.120

    TITLE    = 'System Name'
    CATEGORY = 'Information'
    TYPE     = 'clp'
    SQL         = ''
    CMD      = ['db2', '-tn', 'get', 'database', 'manager', 'configuration']

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):
        match = False
        
        for line in results[0].split('\n'):
            if '(DB2SYSTEM)' in line:
                match                 = True
                value                 = line.split('=')[1].strip()
                self.result['output'] = line
                self.result['level']  = 'GREEN'

        if not match:
            self.result['level']  = 'YELLOW'
            self.result['output'] = 'Setting not found.'
        
        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
