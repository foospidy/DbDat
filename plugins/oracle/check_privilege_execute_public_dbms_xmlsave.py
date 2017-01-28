class check_privilege_execute_public_dbms_xmlsave():
    """
    check_privilege_execute_public_dbms_xmlsave:
    Ensure 'EXECUTE' is revoked from 'PUBLIC' on 'DBMS_XMLSAVE'
    The DBMS_XMLSAVE package accepts a table name and XML as input and 
    then inserts into or updates that table.
    """
    # References:
    # http://www.davidlitchfield.com/AddendumtotheOracle12cCISGuidelines.pdf
    # http://www.davidlitchfield.com/DBMS_XMLSTORE_PLSQL_Injection.pdf

    TITLE    = 'Public Execute DBMS XMLSAVE'
    CATEGORY = 'Privilege'
    TYPE     = 'sql'
    SQL      = "SELECT GRANTEE FROM DBA_TAB_PRIVS WHERE TABLE_NAME = 'DBMS_XMLSAVE' AND GRANTEE = 'PUBLIC' AND PRIVILEGE = 'EXECUTE'"

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):
        self.result['level']  = 'GREEN'
        output                = ''

        for rows in results:
            for row in rows:
                self.result['level'] = 'RED'
                output += 'Execute on DBMS_XMLSAVE granted to ' + row[0] + '\n'

        if 'GREEN' == self.result['level']:
            output = 'PUBLIC not granted Execute DBMS_XMLSAVE.'

        self.result['output'] = output

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
