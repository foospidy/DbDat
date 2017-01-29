class check_privilege_revoke_all_radm():
    """
    check_privilege_revoke_all_radm
    Ensure 'ALL' Is Revoked from Unauthorized 'GRANTEE' on RADM$. 
    The RADM$ table contains a column that contains SQL which will execute when 
    a table is accessed and that table has a redaction policy defined for it.
    """
    # References:
    # http://www.davidlitchfield.com/AddendumtotheOracle12cCISGuidelines.pdf
    # http://www.davidlitchfield.com/oracle_backdoors.pdf
    
    TITLE    = 'Revoke ALL from RLS$'
    CATEGORY = 'Privilege'
    TYPE     = 'sql'
    SQL      = "SELECT GRANTEE, PRIVILEGE FROM DBA_TAB_PRIVS WHERE TABLE_NAME = 'RADM$'"

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):
        self.result['level']  = 'GREEN'
        output                = ''

        for rows in results:
            for row in rows:
                self.result['level'] = 'RED'
                output += row[0] + ' with ' + row[1] + 'on RADM$\n'

        if 'GREEN' == self.result['level']:
            output = 'No user with grants to RADM$.'

        self.result['output'] = output

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
