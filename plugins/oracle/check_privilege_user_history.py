
class check_privilege_user_history():
    """
    check_privilege_user_history:
    The Oracle database SYS.USER_HISTORY$ table contains all the audit records
    for the user's password change history.  (This table gets updated by
    password changes if the user has an assigned profile that has password reuse
    limit set, e.g., PASSWORD_REUSE_TIME set to other than UNLIMITED.)
    """
    # References:
    # https://benchmarks.cisecurity.org/downloads/show-single/?file=oracle11gR2.210

    TITLE    = 'Privileges On USER_HISTORY$'
    CATEGORY = 'Privilege'
    TYPE     = 'sql'
    SQL         = "SELECT grantee, privilege FROM dba_tab_privs WHERE table_name='USER_HISTORY$'"

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):
        self.result['level']  = 'GREEN'
        output                = ''

        for rows in results:
            for row in rows:
                self.result['level'] = 'YELLOW'
                output += 'Privileges On USER_HISTORY$ (%s) granted to %s\n' % (row[1], row[0])

        if 'GREEN' == self.result['level']:
            output = 'No users granted Privileges On USER_HISTORY$.'

        self.result['output'] = output

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
