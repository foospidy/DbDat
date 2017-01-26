class check_privilege_java_allpermission():
    """
    check_privilege_java_allpermission:
    Ensure java.security.AllPermission is revoked from unauthorized 'GRANTEE'.
    The java.security.AllPermission grants all permissions and should not be used.
    """
    # References:
    # http://www.davidlitchfield.com/AddendumtotheOracle12cCISGuidelines.pdf
    # https://docs.oracle.com/database/121/JJDEV/chten.htm#CBBIHIGI
    # https://docs.oracle.com/javase/7/docs/api/java/security/AllPermission.html

    TITLE    = 'java.securityAllPermission'
    CATEGORY = 'Privilege'
    TYPE     = 'sql'
    SQL      = "SELECT GRANTEE FROM DBA_JAVA_POLICY WHERE TYPE_NAME = 'java.security.AllPermission' AND KIND = 'GRANT' AND ENABLED='ENABLED' AND GRANTEE != 'SYS'"

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):
        self.result['level']  = 'GREEN'
        output                = ''

        for rows in results:
            for row in rows:
                self.result['level'] = 'RED'
                output += 'User granted java.securityAllPermission: ' + row[0] + '\n'

        if 'GREEN' == self.result['level']:
            output = 'No user granted java.securityAllPermission.'

        self.result['output'] = output

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
