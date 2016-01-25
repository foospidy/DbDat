class check_privilege_external_quiesceconnect():
    """
    check_privilege_external_quiesceconnect:
    The QUIESCECONNECT role grants the authority to a user to access a database even in the
    quiesced state. It is recommended that the quiesce connect role be granted to authorized
    users only.
    """
    # References:
    # https://benchmarks.cisecurity.org/downloads/show-single/?file=db2.120

    TITLE    = 'QUIESCECONNECTAUTH Role'
    CATEGORY = 'Privilege'
    TYPE     = 'sql'
    SQL         = "SELECT DISTINCT grantee, granteetype FROM syscat.dbauth WHERE quiesceconnectauth='Y'"

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):
        output = ''
        self.result['level']  = 'GREEN'

        for rows in results:
            for row in rows:
                self.result['level']  = 'YELLOW'
                output += 'QUIESCECONNECTAUTH granted to %s\n' % (row[0])

        if 'GREEN' == self.result['level']:
            output = 'No users granted QUIESCECONNECTAUTH.'

        self.result['output'] = output

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
