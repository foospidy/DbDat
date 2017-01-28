class check_privilege_public_system():
    """
    check_privilege_public_system
    Ensure 'PUBLIC' has not been granted a system privilege. 
    By default, PUBLIC is not assigned any system privileges. 
    This check is to ensure this default is still in place.
    """
    # References:
    # http://www.davidlitchfield.com/AddendumtotheOracle12cCISGuidelines.pdf
    
    TITLE    = 'PUBLIC DBA_SYS_PRIVS'
    CATEGORY = 'Privilege'
    TYPE     = 'sql'
    SQL      = "SELECT PRIVILEGE FROM DBA_SYS_PRIVS WHERE GRANTEE = 'PUBLIC'"

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
            output = 'PUBLIC not granted any DBA_SYS_PRIVS.'

        self.result['output'] = output

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
