class check_configuration_remote_access():
    """
    check_configuration_remote_access:
    Enables the execution of local stored procedures on remote servers or remote
    stored procedures on local server.
    """
    # References:
    # https://benchmarks.cisecurity.org/downloads/show-single/index.cfm?file=sql2012DB.120

    TITLE    = 'Remote Access'
    CATEGORY = 'Configuration'
    TYPE     = 'sql'
    SQL         = "SELECT name, CAST(value as int) as value_configured, CAST(value_in_use as int) as value_in_use FROM sys.configurations WHERE name='Remote access'"

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):

        for rows in results:
            for row in rows:
                if 0 == row[1]:
                    self.result['level']  = 'GREEN'
                    self.result['output'] = 'Remote access is (%s) not enabled.' % (row[1])
                else:
                    self.result['level']  = 'RED'
                    self.result['output'] = 'Remote access is (%s) enabled.' % (row[1])

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
