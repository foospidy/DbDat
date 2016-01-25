class check_privilege_dbadm():
    """
    check_privilege_dbadm:
    The DBADM (database administration) role grants the authority to a user to perform
    administrative tasks on a specific database. It is recommended that dbadm role be granted
    to authorized users only.

    """
    # References:
    # https://benchmarks.cisecurity.org/downloads/show-single/?file=db2.120

    TITLE    = 'DBADM Role'
    CATEGORY = 'Privilege'
    TYPE     = 'sql'
    SQL         = "SELECT DISTINCT grantee, granteetype FROM syscat.dbauth WHERE dbadmauth='Y'"

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):
        output = ''
        self.result['level']  = 'GREEN'

        for rows in results:
            for row in rows:
                self.result['level']  = 'YELLOW'
                output += 'DBADM granted to %s\n' % (row[0])

        if 'GREEN' == self.result['level']:
            output = 'No users granted DBADM.'

        self.result['output'] = output

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
