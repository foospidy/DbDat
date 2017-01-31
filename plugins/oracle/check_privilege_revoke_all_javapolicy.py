class check_privilege_revoke_all_javapolicy():
    """
    check_privilege_revoke_all_javapolicy
    Ensure 'ALL' Is Revoked from Unauthorized 'GRANTEE' on JAVA$POLICY$
    The JAVA$POLICY$ table contains details about which users and roles have 
    been granted what Java permissions.
    """
    # References:
    # http://www.davidlitchfield.com/AddendumtotheOracle12cCISGuidelines.pdf
    # http://www.davidlitchfield.com/oracle_backdoors.pdf
    
    TITLE    = 'Revoke ALL from JAVA$POLICY$'
    CATEGORY = 'Privilege'
    TYPE     = 'sql'
    SQL      = "SELECT GRANTEE, PRIVILEGE FROM DBA_TAB_PRIVS WHERE TABLE_NAME = 'JAVA$POLICY$'"

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):
        self.result['level']  = 'GREEN'
        output                = ''

        for rows in results:
            for row in rows:
                self.result['level'] = 'RED'
                output += row[0] + ' with ' + row[1] + 'on JAVA$POLICY$\n'

        if 'GREEN' == self.result['level']:
            output = 'No user with grants to JAVA$POLICY$.'

        self.result['output'] = output

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
