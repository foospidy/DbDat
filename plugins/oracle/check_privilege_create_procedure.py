class check_privilege_create_procedure():
    """
    check_privilege_create_procedure:
    The Oracle database CREATE PROCEDURE privilege allows the designated user
    to create a stored procedure that will fire when given the correct command
    sequence.
    """
    # References:
    # https://benchmarks.cisecurity.org/downloads/show-single/?file=oracle11gR2.210

    TITLE    = 'Create Procedure'
    CATEGORY = 'Privilege'
    TYPE     = 'sql'
    SQL         = "SELECT grantee, privilege FROM dba_sys_privs WHERE privilege='CREATE PROCEDURE' AND grantee NOT IN ('DBA','DBSNMP','MDSYS','OLAPSYS','OWB$CLIENT','OWBSYS','RECOVERY_CATALOG_OWNER','SPATIAL_CSW_ADMIN_USR','SPATIAL_WFS_ADMIN_USR','SYS','APEX_030200','APEX_040000','APEX_040100','APEX_040200')"

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):
        self.result['level']  = 'GREEN'
        output                = ''

        for rows in results:
            for row in rows:
                self.result['level'] = 'YELLOW'
                output += 'Create Procedure granted to ' + row[0] + '\n'

        if 'GREEN' == self.result['level']:
            output = 'No users granted Create Procedure.'

        self.result['output'] = output

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
