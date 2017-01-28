class check_privilege_execute_public_dbms_aw():
    """
    check_privilege_execute_public_dbms_aw:
    Ensure 'EXECUTE' is revoked from 'PUBLIC' on 'DBMS_AW'
    The DBMS_AW package contains procedures and functions for interacting 
    with Analytic Workspaces. Several functions accept OLAP DML as input 
    which can be used to execute SQL.
    """
    # References:
    # http://www.davidlitchfield.com/AddendumtotheOracle12cCISGuidelines.pdf
    # http://www.davidlitchfield.com/ExploitingPLSQLInjectionCREATESESSION.pdf

    TITLE    = 'Public Execute DBMS AW'
    CATEGORY = 'Privilege'
    TYPE     = 'sql'
    SQL      = "SELECT GRANTEE FROM DBA_TAB_PRIVS WHERE TABLE_NAME = 'DBMS_AW' AND GRANTEE = 'PUBLIC' AND PRIVILEGE = 'EXECUTE'"

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):
        self.result['level']  = 'GREEN'
        output                = ''

        for rows in results:
            for row in rows:
                self.result['level'] = 'RED'
                output += 'Execute on DBMS_AW granted to ' + row[0] + '\n'

        if 'GREEN' == self.result['level']:
            output = 'PUBLIC not granted Execute DBMS_AW.'

        self.result['output'] = output

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
