class check_privilege_revoke_all_fga():
    """
    check_privilege_revoke_all_fga
    Ensure 'ALL' Is Revoked from Unauthorized 'GRANTEE' on FGA$. 
    The FGA$ table contains columns that contains the schema and name of a procedure to 
    execute when a table is accessed and that has a Fine Grained Auditing policy defined 
    for it.
    """
    # References:
    # http://www.davidlitchfield.com/AddendumtotheOracle12cCISGuidelines.pdf
    # http://www.davidlitchfield.com/oracle_backdoors.pdf
    
    TITLE    = 'Revoke ALL from FGA$'
    CATEGORY = 'Privilege'
    TYPE     = 'sql'
    SQL      = "SELECT GRANTEE, PRIVILEGE FROM DBA_TAB_PRIVS WHERE TABLE_NAME = 'FGA$'"

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):
        self.result['level']  = 'GREEN'
        output                = ''

        for rows in results:
            for row in rows:
                self.result['level'] = 'RED'
                output += row[0] + ' with ' + row[1] + 'on FGA$\n'

        if 'GREEN' == self.result['level']:
            output = 'No user with grants to FGA$.'

        self.result['output'] = output

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
