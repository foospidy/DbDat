class check_configuration_dftdbpath():
    """
    check_configuration_dftdbpath:
    The dftdbpath parameter contains the default file path used to create DB2 databases. It is
    recommended that this parameter is set to a directory that is owned by the DB2
    Administrator
    """
    # References:
    # https://benchmarks.cisecurity.org/downloads/show-single/?file=db2.120

    TITLE    = 'Default Database Location'
    CATEGORY = 'Configuration'
    TYPE     = 'clp'
    SQL         = ''
    CMD      = ['db2', '-tn', 'get', 'database', 'manager', 'configuration']

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):
        self.result['level']  = 'GRAY'
        self.result['output'] = 'DFTDBPATH setting not found'

        for line in results[0].split('\n'):
            if '(DFTDBPATH)' in line:
                value                 = line.split('=')[1].strip()
                self.result['output'] = line
                self.result['level']  = 'YELLOW'

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
