class check_configuration_discover_inst():
    """
    check_configuration_discover_inst:
    The discover_inst parameter specifies whether the instance can be discovered in the
    network. It is recommended that instances notbe discoverable.
    """
    # References:
    # https://benchmarks.cisecurity.org/downloads/show-single/?file=db2.120

    TITLE    = 'Discover Instance'
    CATEGORY = 'Configuration'
    TYPE     = 'clp'
    SQL         = ''
    CMD      = ['db2', '-tn', 'get', 'database', 'manager', 'configuration']

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):
        for line in results[0].split('\n'):
            if '(DISCOVER_INST)' in line:
                value                 = line.split('=')[1].strip()
                self.result['output'] = line

                if 'DISABLE' == value:
                    self.result['level'] = 'GREEN'
                else:
                    self.result['level'] = 'RED'

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
