class check_privilege_revoke_all_trigger():
    """
    check_privilege_revoke_all_trigger
    Ensure 'ALL' Is Revoked from Unauthorized 'GRANTEE' on TRIGGER$
    The ACTION# column of the TRIGGER$ table contains contains the SQL 
    of each trigger.
    """
    # References:
    # http://www.davidlitchfield.com/AddendumtotheOracle12cCISGuidelines.pdf
    # http://www.davidlitchfield.com/oracle_backdoors.pdf
    
    TITLE    = 'Revoke ALL from TRIGGER$'
    CATEGORY = 'Privilege'
    TYPE     = 'sql'
    SQL      = "SELECT GRANTEE, PRIVILEGE FROM DBA_TAB_PRIVS WHERE TABLE_NAME = 'TRIGGER$'"

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):
        self.result['level']  = 'GREEN'
        output                = ''

        for rows in results:
            for row in rows:
                self.result['level'] = 'RED'
                output += row[0] + ' with ' + row[1] + 'on TRIGGER$\n'

        if 'GREEN' == self.result['level']:
            output = 'No user with grants to TRIGGER$.'

        self.result['output'] = output

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
