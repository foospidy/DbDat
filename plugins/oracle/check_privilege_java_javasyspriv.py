class check_privilege_java_javasyspriv():
    """
    check_privilege_java_javasyspriv:
    Ensure membership of the JAVASYSPRIV role is revoked from unauthorized 'GRANTEE'.
    The JAVASYSPRIV role has a larger number of very powerful Java permissions. Membership 
    of this role should be tightly controlled. Ensure that only trusted users have membership.
    """
    # References:
    # http://www.davidlitchfield.com/AddendumtotheOracle12cCISGuidelines.pdf
    # https://docs.oracle.com/database/121/JJDEV/chten.htm#JJDEV13325

    TITLE    = 'JAVASYSPRIV'
    CATEGORY = 'Privilege'
    TYPE     = 'sql'
    SQL      = "SELECT GRANTEE FROM DBA_ROLE_PRIVS WHERE GRANTED_ROLE = 'JAVASYSPRIV' AND GRANTEE != 'SYS'"

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):
        self.result['level']  = 'GREEN'
        output                = ''

        for rows in results:
            for row in rows:
                self.result['level'] = 'RED'
                output += 'User granted JAVASYSPRIV: ' + row[0] + '\n'

        if 'GREEN' == self.result['level']:
            output = 'No user in the role JAVASYSPRIV.'

        self.result['output'] = output

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
