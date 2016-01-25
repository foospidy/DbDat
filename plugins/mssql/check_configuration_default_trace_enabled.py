class check_configuration_default_trace_enabled():
    """
    check_configuration_default_trace_enabled:
    The default trace provides audit logging of database activity including
    account creations, privilege elevation and execution of DBCC commands.
    """
    # References:
    # https://benchmarks.cisecurity.org/downloads/show-single/index.cfm?file=sql2012DB.120

    TITLE    = 'Default Trace Enabled'
    CATEGORY = 'Configuration'
    TYPE     = 'sql'
    SQL         = "SELECT name, CAST(value as int) as value_configured, CAST(value_in_use as int) as value_in_use FROM sys.configurations WHERE name='Default trace enabled'"

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):

        for rows in results:
            for row in rows:
                if 0 == row[1]:
                    self.result['level']  = 'RED'
                    self.result['output'] = 'Default Trace is (%s) not enabled.' % (row[1])
                else:
                    self.result['level']  = 'GREEN'
                    self.result['output'] = 'Default Trace is (%s) enabled.' % (row[1])

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
