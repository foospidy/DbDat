class check_privilege_revoke_all_col():
    """
    check_privilege_revoke_all_col
    Ensure 'ALL' Is Revoked from Unauthorized 'GRANTEE' on COL$
    The DEFAULT$ column of the COL$ table contains the SQL for tables with virtual 
    columns and function-based indexes.
    """
    # References:
    # http://www.davidlitchfield.com/AddendumtotheOracle12cCISGuidelines.pdf
    # http://www.davidlitchfield.com/oracle_backdoors.pdf
    
    TITLE    = 'Revoke ALL from COL$'
    CATEGORY = 'Privilege'
    TYPE     = 'sql'
    SQL      = "SELECT GRANTEE, PRIVILEGE FROM DBA_TAB_PRIVS WHERE TABLE_NAME = 'COL$'"

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):
        self.result['level']  = 'GREEN'
        output                = ''

        for rows in results:
            for row in rows:
                self.result['level'] = 'RED'
                output += row[0] + ' with ' + row[1] + 'on COL$\n'

        if 'GREEN' == self.result['level']:
            output = 'No user with grants to COL$.'

        self.result['output'] = output

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
