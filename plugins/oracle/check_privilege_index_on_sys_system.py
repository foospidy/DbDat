
class check_privilege_index_on_sys_system():
    """
    check_privilege_index_on_sys_system:
    Ensure no user has the INDEX privilege on SYS or SYSTEM owned tables
    A user may create an index on a table owned by another user if they 
    have the INDEX privilege on the table in question.
    """
    # References:
    # http://www.davidlitchfield.com/AddendumtotheOracle12cCISGuidelines.pdf
    # http://www.davidlitchfield.com/Privilege_Escalation_via_Oracle_Indexes.pdf

    TITLE    = 'No INDEX on SYS or SYSTEM'
    CATEGORY = 'Privilege'
    TYPE     = 'sql'
    SQL      = "SELECT GRANTEE, OWNER, TABLE_NAME FROM DBA_TAB_PRIVS WHERE PRIVILEGE = 'INDEX' AND OWNER IN ('SYS', 'SYSTEM')"

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):
        self.result['level']  = 'GREEN'
        output                = ''

        for rows in results:
            for row in rows:
                self.result['level'] = 'RED'
                output += 'INDEX privilege granted to (%s) on %s: %s\n' % (row[0], row[1], row[2])

        if 'GREEN' == self.result['level']:
            output = 'No user has INDEX privilege on SYS or SYSTEM owned tables.'

        self.result['output'] = output

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
