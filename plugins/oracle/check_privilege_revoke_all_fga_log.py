class check_privilege_revoke_all_fga_log():
    """
    check_privilege_revoke_all_fga_log
    Ensure 'ALL' Is Revoked from Unauthorized 'GRANTEE' on FGA_LOG$
    The FGA_LOG$ table contains audit records for tables with a defined Fine 
    Grained Auditing policy.
    """
    # References:
    # http://www.davidlitchfield.com/AddendumtotheOracle12cCISGuidelines.pdf
    # http://www.davidlitchfield.com/oracle_backdoors.pdf
    
    TITLE    = 'Revoke ALL from FGA_LOG$'
    CATEGORY = 'Privilege'
    TYPE     = 'sql'
    SQL      = "SELECT GRANTEE, PRIVILEGE FROM DBA_TAB_PRIVS WHERE TABLE_NAME = 'FGA_LOG$'"

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):
        self.result['level']  = 'GREEN'
        output                = ''

        for rows in results:
            for row in rows:
                self.result['level'] = 'RED'
                output += row[0] + ' with ' + row[1] + 'on FGA_LOG$\n'

        if 'GREEN' == self.result['level']:
            output = 'No user with grants to FGA_LOG$.'

        self.result['output'] = output

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
