class check_configuration_dbms_sql_security_level():
    """
    check_configuration_dbms_sql_security_level
    Ensure _dbms_sql_security_level is set to 1 or 2.
    The _dbms_sql_security_level parameter controls how access to cursors 
    used by DBMS_SQL is controlled. The default setting of 1 ensures that 
    the effective user ID for both parse and execute operations are the same; 
    this prevents cursor snarfing attacks. A setting 2 is more restrictive; a 
    setting of 0 or 384 turns off security checks thus opening the server to 
    cursor snarfing attacks.
    """
    # References:
    # http://www.davidlitchfield.com/AddendumtotheOracle12cCISGuidelines.pdf

    TITLE    = 'DBMS SQL Security Level'
    CATEGORY = 'Configuration'
    TYPE     = 'sql'
    SQL      = "SELECT c.ksppstvl FROM x$ksppi a, x$ksppsv c WHERE a.indx = c.indx AND a.ksppinm = '_dbms_sql_security_level'"

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):

        for rows in results:
            for row in rows:
                if int(row[0]) not in [1, 2]:
                    self.result['level']  = 'RED'
                    self.result['output'] = 'DBMS SQL Security Level is (%s).' % (row[0])
                else:
                    self.result['level']  = 'GREEN'
                    self.result['output'] = 'DBMS SQL Security Level is (%s).' % (row[0])

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
