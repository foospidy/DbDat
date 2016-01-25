class check_privilege_nofence():
    """
    check_privilege_nofence:
    The NOFENCE role grants the authority to a user to create user-defined functions or
    procedures that are not fenced in the memory block of the database. It is recommended
    that the nofence role be granted to authorized users only.
    """
    # References:
    # https://benchmarks.cisecurity.org/downloads/show-single/?file=db2.120

    TITLE    = 'NOFENCEAUTH Role'
    CATEGORY = 'Privilege'
    TYPE     = 'sql'
    SQL         = "SELECT DISTINCT grantee, granteetype FROM syscat.dbauth WHERE nofenceauth='Y'"

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):
        output = ''
        self.result['level']  = 'GREEN'

        for rows in results:
            for row in rows:
                self.result['level']  = 'YELLOW'
                output += 'NOFENCEAUTH granted to %s\n' % (row[0])

        if 'GREEN' == self.result['level']:
            output = 'No users granted NOFENCEAUTH.'

        self.result['output'] = output

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
