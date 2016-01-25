class check_privilege_connect():
    """
    check_privilege_connect:
    The CONNECT role grants the authority to a user to connect to a specific database. It is
    recommended that connect role be granted to authorized users only.
    """
    # References:
    # https://benchmarks.cisecurity.org/downloads/show-single/?file=db2.120

    TITLE    = 'CONNECTAUTH Role'
    CATEGORY = 'Privilege'
    TYPE     = 'sql'
    SQL         = "SELECT DISTINCT grantee, granteetype FROM syscat.dbauth WHERE connectauth='Y'"

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):
        output = ''
        self.result['level']  = 'GREEN'

        for rows in results:
            for row in rows:
                self.result['level']  = 'YELLOW'
                output += 'CONNECTAUTH granted to %s\n' % (row[0])

        if 'GREEN' == self.result['level']:
            output = 'No users granted CONNECTAUTH.'

        self.result['output'] = output

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
