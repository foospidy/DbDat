class check_privilege_revoke_all_context():
    """
    check_privilege_revoke_all_context
    Ensure 'ALL' Is Revoked from Unauthorized 'GRANTEE' on CONTEXT$
    The CONTEXT$ table contains columns for the schema and name for a PL/SQL 
    package that will execute for a given application context.
    """
    # References:
    # http://www.davidlitchfield.com/AddendumtotheOracle12cCISGuidelines.pdf
    # http://www.davidlitchfield.com/oracle_backdoors.pdf
    
    TITLE    = 'Revoke ALL from CONTEXT$'
    CATEGORY = 'Privilege'
    TYPE     = 'sql'
    SQL      = "SELECT GRANTEE, PRIVILEGE FROM DBA_TAB_PRIVS WHERE TABLE_NAME = 'CONTEXT$'"

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):
        self.result['level']  = 'GREEN'
        output                = ''

        for rows in results:
            for row in rows:
                self.result['level'] = 'RED'
                output += row[0] + ' with ' + row[1] + 'on CONTEXT$\n'

        if 'GREEN' == self.result['level']:
            output = 'No user with grants to CONTEXT$.'

        self.result['output'] = output

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
