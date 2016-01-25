
class check_privilege_sys_scheduler_credential():
    """
    check_privilege_sys_scheduler_credential:
    The Oracle database SCHEDULER$_CREDENTIAL table contains the database
    scheduler credential information.
    """
    # References:
    # https://benchmarks.cisecurity.org/downloads/show-single/?file=oracle11gR2.210

    TITLE    = 'Privileges On SCHEDULER$_CREDENTIAL'
    CATEGORY = 'Privilege'
    TYPE     = 'sql'
    SQL         = "SELECT grantee, privilege FROM dba_tab_privs WHERE table_name='SCHEDULER$_CREDENTIAL'"

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):
        self.result['level']  = 'GREEN'
        output                = ''

        for rows in results:
            for row in rows:
                self.result['level'] = 'YELLOW'
                output += 'Privileges On SCHEDULER$_CREDENTIAL (%s) granted to %s\n' % (row[1], row[0])

        if 'GREEN' == self.result['level']:
            output = 'No users granted Privileges On SCHEDULER$_CREDENTIAL.'

        self.result['output'] = output

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
