class check_privilege_select_dynamic_performance_views():
    """
    check_privilege_select_dynamic_performance_views:
    Ensure SELECT on Dynamic Performance Views that contain SQL is revoked from 
    unauthorized 'GRANTEE'.
    A number of dynamic views contain previously executed SQL and values for bind 
    variables. These may contain highly sensitive information.
    """
    # References:
    # http://www.davidlitchfield.com/AddendumtotheOracle12cCISGuidelines.pdf

    TITLE    = 'Select Dynamic Performance Views'
    CATEGORY = 'Privilege'
    TYPE     = 'sql'
    SQL         = "SELECT GRANTEE||':'||TABLE_NAME FROM DBA_TAB_PRIVS WHERE TABLE_NAME IN ('V_$SQL', 'GV_$SQL', 'V_$SQLTEXT', 'GV_$SQLTEXT', 'V_$SQLTEXT_WITH_NEWLINES', 'GV_$SQLTEXT_WITH_NEWLINES', 'V_$SQLAREA', 'GV_$SQLAREA', 'V_$SQL_SHARED_MEMORY', 'GV_$SQL_SHARED_MEMORY', 'V_$SQLAREA_PLAN_HASH', 'GV_$SQLAREA_PLAN_HASH', 'V_$SQLSTATS', 'GV_$SQLSTATS', 'WRH$_SQLTEXT', 'WRI$_ADV_SQLW_STMTS')"

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):
        self.result['level']  = 'GREEN'
        output                = ''

        for rows in results:
            for row in rows:
                self.result['level'] = 'RED'
                output += 'Select on dynamic performance views granted to ' + row[0] + '\n'

        if 'GREEN' == self.result['level']:
            output = 'No users granted Select on dynamic performance views.'

        self.result['output'] = output

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
