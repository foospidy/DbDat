class check_privilege_java_filepermission_write():
    """
    check_privilege_java_filepermission_write:
    Ensure wildcard java.io.FilePermission.write is revoked from unauthorized 'GRANTEE'.
    The write action of the java.io.FilePermission grants the ability to write files to 
    the OS.
    """
    # References:
    # http://www.davidlitchfield.com/AddendumtotheOracle12cCISGuidelines.pdf
    # https://docs.oracle.com/database/121/JJDEV/chten.htm#CBBIHIGI

    TITLE    = 'java.io.FilePermission.write'
    CATEGORY = 'Privilege'
    TYPE     = 'sql'
    SQL      = "SELECT GRANTEE FROM DBA_JAVA_POLICY WHERE TYPE_NAME = 'java.io.FilePermission' AND ACTION LIKE '%write%' AND NAME='<<ALL FILES>>' AND KIND = 'GRANT' AND ENABLED='ENABLED' AND GRANTEE != 'JAVASYSPRIV'"

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):
        self.result['level']  = 'GREEN'
        output                = ''

        for rows in results:
            for row in rows:
                self.result['level'] = 'RED'
                output += 'User with write action for the java.io.FilePermission: ' + row[0] + '\n'

        if 'GREEN' == self.result['level']:
            output = 'No user has the write action for the java.io.FilePermission.'

        self.result['output'] = output

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
