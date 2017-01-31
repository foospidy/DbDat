
class check_privilege_execute_dbms_pdb_exec_sql():
    """
    check_privilege_execute_dbms_pdb_exec_sql.
    The DBMS_PDB_EXEC_SQL procedure takes an SQL query as a parameter 
    and executes it.
    """
    # References:
    # http://www.davidlitchfield.com/AddendumtotheOracle12cCISGuidelines.pdf
    
    TITLE    = 'Execute on DBMS_PDB_EXEC_SQL'
    CATEGORY = 'Privilege'
    TYPE     = 'sql'
    SQL      = "SELECT GRANTEE FROM DBA_TAB_PRIVS WHERE TABLE_NAME = 'DBMS_PDB_EXEC_SQL' AND PRIVILEGE = 'EXECUTE'"

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):
        self.result['level']  = 'GREEN'
        output                = ''

        for rows in results:
            for row in rows:
                self.result['level'] = 'RED'
                output += 'Execute on DBMS_PDB_EXEC_SQL granted to %s\n' % (row[0])

        if 'GREEN' == self.result['level']:
            output = 'Execute on DBMS_PDB_EXEC_SQL not granted to user any user.'

        self.result['output'] = output

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
