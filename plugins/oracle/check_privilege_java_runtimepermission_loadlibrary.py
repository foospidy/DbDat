class check_privilege_java_runtimepermission_loadlibrary():
    """
    check_privilege_java_runtimepermission_loadlibrary:
    Ensure java.lang.RuntimePermission.loadLibrary is revoked from unauthorized 'GRANTEE'.
    The loadLibrary permission allows grantees to load OS libraries into the server's address space.
    """
    # References:
    # http://www.davidlitchfield.com/AddendumtotheOracle12cCISGuidelines.pdf
    # https://docs.oracle.com/database/121/JJDEV/chten.htm#CBBIHIGI
    # http://www.davidlitchfield.com/oracle_backdoors.pdf

    TITLE    = 'java.lang.RuntimePermission.loadLibrary'
    CATEGORY = 'Privilege'
    TYPE     = 'sql'
    SQL      = "SELECT GRANTEE, NAME, SEQ FROM DBA_JAVA_POLICY WHERE TYPE_NAME = 'java.lang.RuntimePermission' AND NAME LIKE '%loadLibrary%' AND KIND = 'GRANT' AND ENABLED='ENABLED' AND GRANTEE NOT IN ('SYS', 'ORDSYS')"

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):
        self.result['level']  = 'GREEN'
        output                = ''

        for rows in results:
            for row in rows:
                self.result['level'] = 'RED'
                output += 'User with loadlibrary action for the java.lang.RuntimePermission: ' + row[0] + '\n'

        if 'GREEN' == self.result['level']:
            output = 'No user has the loadlibrary action for the java.lang.RuntimePermission.'

        self.result['output'] = output

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
