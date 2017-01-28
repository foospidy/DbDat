class check_privilege_public_directories():
    """
    check_privilege_public_directories
    Ensure 'PUBLIC' does not have write access to any directories. 
    An Oracle directory object gives a user access to the server's 
    file system when using UTL_FILE or BFILENAME.
    """
    # References:
    # http://www.davidlitchfield.com/AddendumtotheOracle12cCISGuidelines.pdf
    
    TITLE    = 'PUBLIC DBA_TAB_PRIVS'
    CATEGORY = 'Privilege'
    TYPE     = 'sql'
    SQL      = "SELECT TABLE_NAME FROM DBA_TAB_PRIVS WHERE GRANTEE = 'PUBLIC' AND PRIVILEGE = 'WRITE'"

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):
        self.result['level']  = 'GREEN'
        output                = ''

        for rows in results:
            for row in rows:
                self.result['level'] = 'RED'
                output += 'PUBLIC is granted ' + row[0] + '\n'

        if 'GREEN' == self.result['level']:
            output = 'PUBLIC not granted any DBA_TAB_PRIVS.'

        self.result['output'] = output

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
