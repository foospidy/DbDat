
class check_privilege_dba_sys_privs_with_admin_option():
    """
    check_privilege_dba_sys_privs_with_admin_option:
    The Oracle database WITH_ADMIN privilege allows the designated user to grant
    another user the same privileges.
    """
    # References:
    # https://benchmarks.cisecurity.org/downloads/show-single/?file=oracle11gR2.210

    TITLE    = 'WITH_ADMIN Privileges'
    CATEGORY = 'Privilege'
    TYPE     = 'sql'
    SQL         = "SELECT grantee, privilege FROM dba_sys_privs WHERE admin_option='YES' AND grantee NOT IN ('AQ_ADMINISTRATOR_ROLE','DBA','OWBSYS','SCHEDULER_ADMIN','SYS','SYSTEM','WMSYS')"

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):
        self.result['level']  = 'GREEN'
        output                = ''

        for rows in results:
            for row in rows:
                self.result['level'] = 'YELLOW'
                output += 'WITH_ADMIN Privilege granted to %s\n' % (row[0])

        if 'GREEN' == self.result['level']:
            output = 'No user found with WITH_ADMIN Privilege.'

        self.result['output'] = output

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
