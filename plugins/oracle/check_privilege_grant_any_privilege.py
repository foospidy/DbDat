class check_privilege_grant_any_privilege():
    """
    check_privilege_grant_any_privilege:
    The    Oracle database GRANT ANY PRIVILEGE keyword provides the grantee the
    capability to grant any single privilege to any item in the catalog of
    the database.
    """
    # References:
    # https://benchmarks.cisecurity.org/downloads/show-single/?file=oracle11gR2.210

    TITLE    = 'Grant Any Privilege'
    CATEGORY = 'Privilege'
    TYPE     = 'sql'
    SQL         = "SELECT grantee, privilege FROM dba_sys_privs WHERE privilege='GRANT ANY PRIVILEGE' AND grantee NOT IN ('DBA','SYS','IMP_FULL_DATABASE','DATAPUMP_IMP_FULL_DATABASE')"

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):
        self.result['level']  = 'GREEN'
        output                = ''

        for rows in results:
            for row in rows:
                self.result['level'] = 'YELLOW'
                output += 'Grant Any Privilege granted to ' + row[0] + '\n'

        if 'GREEN' == self.result['level']:
            output = 'No users granted Grant Any Privilege.'

        self.result['output'] = output

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
