class check_privilege_delete_catalog_role():
    """
    check_privilege_delete_catalog_role:
    The Oracle database DELETE_CATALOG_ROLE provides DELETE privileges for the
    records in the system's audit table (AUD$).
    """
    # References:
    # https://benchmarks.cisecurity.org/downloads/show-single/?file=oracle11gR2.210

    TITLE    = 'Delete Catalog Role'
    CATEGORY = 'Privilege'
    TYPE     = 'sql'
    SQL         = "SELECT grantee, granted_role FROM dba_role_privs WHERE granted_role='DELETE CATALOG ROLE' AND grantee NOT IN ('DBA','SYS')"

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):
        self.result['level']  = 'GREEN'
        output                = ''

        for rows in results:
            for row in rows:
                self.result['level'] = 'YELLOW'
                output += 'Delete Catalog Role granted to ' + row[0] + '\n'

        if 'GREEN' == self.result['level']:
            output = 'No users granted Delete Catalog Role.'

        self.result['output'] = output

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
