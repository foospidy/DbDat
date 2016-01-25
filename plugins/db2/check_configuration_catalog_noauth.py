class check_configuration_catalog_noauth():
    """
    check_configuration_catalog_noauth:
    DB2 can be configured to allow users that do not possess the SYSADM authority to catalog
    and uncatalog databases and nodes. It is recommended that the SYSADM authority be
    required to catalog and uncatalog databases and nodes. It is recommended that the
    catalog_noauth parameter be set to NO.
    """
    # References:
    # https://benchmarks.cisecurity.org/downloads/show-single/?file=db2.120

    TITLE    = 'Explicit Authorization for Cataloging'
    CATEGORY = 'Configuration'
    TYPE     = 'clp'
    SQL         = ''
    CMD      = ['db2', '-tn', 'get', 'database', 'manager', 'configuration']

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):
        for line in results[0].split('\n'):
            if '(CATALOG_NOAUTH)' in line:
                value                 = line.split('=')[1].strip()
                self.result['output'] = line

                if 'NO' == value:
                    self.result['level'] = 'GREEN'
                else:
                    self.result['level'] = 'RED'

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
