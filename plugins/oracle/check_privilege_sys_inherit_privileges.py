
class check_privilege_sys_inherit_privileges():
    """
    check_privilege_sys_inherit_privileges:
    The INHERIT PRIVILEGES privilege allows the owner of an invoker rights procedure 
    to inherit the privileges of the invoker during the execution of the procedure. 
    By default, no user should have this privilege
    """
    # References:
    # http://www.davidlitchfield.com/AddendumtotheOracle12cCISGuidelines.pdf
    # http://docs.oracle.com/database/121/DBSEG/dr_ir.htm#DBSEG658

    TITLE    = 'SYS no INHERIT PRIVILEGES'
    CATEGORY = 'Privilege'
    TYPE     = 'sql'
    SQL      = "SELECT TABLE_NAME, GRANTEE FROM DBA_TAB_PRIVS WHERE PRIVILEGE='INHERIT PRIVILEGES' AND GRANTEE='SYS'"

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):
        self.result['level']  = 'GREEN'
        output                = ''

        for rows in results:
            for row in rows:
                self.result['level'] = 'RED'
                output += 'Privileges On SYS INHERIT PRIVILEGES (%s) granted to %s\n' % (row[1], row[0])

        if 'GREEN' == self.result['level']:
            output = 'SYS has no INHERIT PRIVILEGES.'

        self.result['output'] = output

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
