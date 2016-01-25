class check_configuration_diagpath():
    """
    check_configuration_diagpath:
    The diagpath parameter specifies the location of the diagnostic files for the DB2 instance.
    It is recommended that this parameter be set to a secure location.
    """
    # References:
    # https://benchmarks.cisecurity.org/downloads/show-single/?file=db2.120

    TITLE    = 'Diag Path'
    CATEGORY = 'Configuration'
    TYPE     = 'clp'
    SQL         = ''
    CMD      = ['db2', '-tn', 'get', 'database', 'manager', 'configuration']

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):
        for line in results[0].split('\n'):
            if '(DIAGPATH)' in line:
                value                 = line.split('=')[1].strip()
                self.result['output'] = line

                if '' != value:
                    self.result['level'] = 'YELLOW'
                else:
                    self.result['level'] = 'RED'

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
