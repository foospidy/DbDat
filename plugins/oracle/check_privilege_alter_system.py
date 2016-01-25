class check_privilege_alter_system():
    """
    check_privilege_alter_system:
    The    Oracle database ALTER SYSTEM privilege allows the designated user to
    dynamically    alter the instance's running operations.
    """
    # References:
    # https://benchmarks.cisecurity.org/downloads/show-single/?file=oracle11gR2.210

    TITLE    = 'Alter System'
    CATEGORY = 'Privilege'
    TYPE     = 'sql'
    SQL         = "SELECT grantee, privilege FROM dba_sys_privs WHERE privilege='ALTER SYSTEM' AND grantee NOT IN ('SYS','SYSTEM','APEX_030200','APEX_040000','APEX_040100','APEX_040200')"

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):
        self.result['level']  = 'GREEN'
        output                = ''

        for rows in results:
            for row in rows:
                self.result['level'] = 'YELLOW'
                output += 'Alter System granted to ' + row[0] + '\n'

        if 'GREEN' == self.result['level']:
            output = 'No users granted Alter System.'

        self.result['output'] = output

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
