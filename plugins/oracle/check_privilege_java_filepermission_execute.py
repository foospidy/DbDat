class check_privilege_java_filepermission_execute():
    """
    check_privilege_java_filepermission_execute:
    Ensure java.io.FilePermission.execute is revoked from unauthorized 'GRANTEE'.
    The execute action for the java.io.FilePermission allows a user to execute OS 
    commands from the Java Runtime.
    """
    # References:
    # http://www.davidlitchfield.com/AddendumtotheOracle12cCISGuidelines.pdf
    # https://docs.oracle.com/database/121/JJDEV/chten.htm#CBBIHIGI

    TITLE    = 'java.io.FilePermission.execute'
    CATEGORY = 'Privilege'
    TYPE     = 'sql'
    SQL      = "SELECT GRANTEE FROM DBA_JAVA_POLICY WHERE TYPE_NAME = 'java.io.FilePermission' AND ACTION LIKE '%execute%' AND (NAME='<<ALL FILES>>' OR NAME LIKE '%*%') AND KIND = 'GRANT' AND ENABLED='ENABLED' AND GRANTEE !='JAVASYSPRIV'"

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):
        self.result['level']  = 'GREEN'
        output                = ''

        for rows in results:
            for row in rows:
                self.result['level'] = 'YELLOW'
                output += 'User with execute action for execute action for the java.io.FilePermission: ' + row[0] + '\n'

        if 'GREEN' == self.result['level']:
            output = 'No GRANTEE has the execute action for the java.io.FilePermission.'

        self.result['output'] = output

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
