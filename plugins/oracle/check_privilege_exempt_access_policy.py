class check_privilege_exempt_access_policy():
    """
    check_privilege_exempt_access_policy:
    The    Oracle database EXEMPT ACCESS POLICY keyword provides the user the
    capability to access all the table rows regardless of row-level security
    lockouts.
    """
    # References:
    # https://benchmarks.cisecurity.org/downloads/show-single/?file=oracle11gR2.210

    TITLE    = 'Exempt Access Policy'
    CATEGORY = 'Privilege'
    TYPE     = 'sql'
    SQL         = "SELECT grantee, privilege FROM dba_sys_privs WHERE privilege='EXEMPT ACCESS POLICY'"

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):
        self.result['level']  = 'GREEN'
        output                = ''

        for rows in results:
            for row in rows:
                self.result['level'] = 'YELLOW'
                output += 'Exempt Access Policy granted to ' + row[0] + '\n'

        if 'GREEN' == self.result['level']:
            output = 'No users granted Exempt Access Policy.'

        self.result['output'] = output

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
