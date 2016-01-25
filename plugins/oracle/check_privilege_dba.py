class check_privilege_dba():
    """
    check_privilege_dba:
    The Oracle database DBA role is the default database administrator role provided
    for the allocation of administrative privileges.
    """
    # References:
    # https://benchmarks.cisecurity.org/downloads/show-single/?file=oracle11gR2.210

    TITLE    = 'DBA'
    CATEGORY = 'Privilege'
    TYPE     = 'sql'
    SQL         = "SELECT grantee, granted_role FROM dba_role_privs WHERE granted_role='DBA' AND grantee NOT IN ('SYS','SYSTEM')"

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):
        self.result['level']  = 'GREEN'
        output                = ''

        for rows in results:
            for row in rows:
                self.result['level'] = 'YELLOW'
                output += 'DBA granted to ' + row[0] + '\n'

        if 'GREEN' == self.result['level']:
            output = 'No users granted DBA.'

        self.result['output'] = output

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
