class check_configuration_skip_merge():
    """
    check_configuration_skip_merge:
    Prevent continued table access using a merge table even after permission
    is revoked. This option will disable use of MERGE tables.
    """
    # References:
    # https://benchmarks.cisecurity.org/downloads/show-single/index.cfm?file=mysql.102

    TITLE    = 'Skip Merge'
    CATEGORY = 'Configuration'
    TYPE     = 'sql'
    SQL         = "SHOW GLOBAL VARIABLES LIKE 'have_merge_engine'"

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):

        for rows in results:
            for row in rows:
                if 'DISABLED' != row[1]:
                    self.result['level']  = 'RED'
                    self.result['output'] = 'Merge is (%s) enabled.' % (row[1])
                else:
                    self.result['level']  = 'GREEN'
                    self.result['output'] = 'Merge is (%s) not enabled.' % (row[1])

            return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
