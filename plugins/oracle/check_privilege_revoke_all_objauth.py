class check_privilege_revoke_all_objauth():
    """
    check_privilege_revoke_all_objauth
    Ensure 'ALL' Is Revoked from Unauthorized 'GRANTEE' on OBJAUTH$
    The OBJAUTH$ table stores details about which users or roles have 
    which privileges on which objects.
    """
    # References:
    # http://www.davidlitchfield.com/AddendumtotheOracle12cCISGuidelines.pdf
    # http://www.davidlitchfield.com/oracle_backdoors.pdf
    
    TITLE    = 'Revoke ALL from OBJAUTH$'
    CATEGORY = 'Privilege'
    TYPE     = 'sql'
    SQL      = "SELECT GRANTEE, PRIVILEGE FROM DBA_TAB_PRIVS WHERE TABLE_NAME = 'OBJAUTH$'"

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):
        self.result['level']  = 'GREEN'
        output                = ''

        for rows in results:
            for row in rows:
                self.result['level'] = 'RED'
                output += row[0] + ' with ' + row[1] + 'on OBJAUTH$\n'

        if 'GREEN' == self.result['level']:
            output = 'No user with grants to OBJAUTH$.'

        self.result['output'] = output

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
