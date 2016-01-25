class check_privilege_bindadd():
    """
    check_privilege_bindadd:
    The BINDADD (bind application) role grants the authority to a user to create packages on a
    specific database. It is recommended thatthe bindadd role be granted to authorizedusers
    only.
    """
    # References:
    # https://benchmarks.cisecurity.org/downloads/show-single/?file=db2.120

    TITLE    = 'BINDADDAUTH Role'
    CATEGORY = 'Privilege'
    TYPE     = 'sql'
    SQL         = "SELECT DISTINCT grantee, granteetype FROM syscat.dbauth WHERE bindaddauth='Y'"

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):
        output = ''
        self.result['level']  = 'GREEN'

        for rows in results:
            for row in rows:
                self.result['level']  = 'YELLOW'
                output += 'BINDADDAUTH granted to %s\n' % (row[0])

        if 'GREEN' == self.result['level']:
            output = 'No users granted BINDADDAUTH.'

        self.result['output'] = output

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
