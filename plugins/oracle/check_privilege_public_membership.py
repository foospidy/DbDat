class check_privilege_public_membership():
    """
    check_privilege_public_membership
    Ensure 'PUBLIC' has not been assigned membership of a role. 
    PUBLIC is not assigned membership of a role by default. This 
    check ensures this default is still in place.
    """
    # References:
    # http://www.davidlitchfield.com/AddendumtotheOracle12cCISGuidelines.pdf
    
    TITLE    = 'PUBLIC Membership'
    CATEGORY = 'Privilege'
    TYPE     = 'sql'
    SQL      = "SELECT GRANTED_ROLE FROM DBA_ROLE_PRIVS WHERE GRANTEE = 'PUBLIC'"

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):
        self.result['level']  = 'GREEN'
        output                = ''

        for rows in results:
            for row in rows:
                self.result['level'] = 'RED'
                output += 'PUBLIC is member of ' + row[0] + '\n'

        if 'GREEN' == self.result['level']:
            output = 'PUBLIC not a member of any role.'

        self.result['output'] = output

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
