class check_configuration_mail_xps():
    """
    check_configuration_mail_xps:
    This option controls the generation and transmission of email messages from
    SQL Server.
    """
    # References:
    # https://benchmarks.cisecurity.org/downloads/show-single/index.cfm?file=sql2012DB.120

    TITLE    = 'Database Mail XPs'
    CATEGORY = 'Configuration'
    TYPE     = 'sql'
    SQL         = "SELECT name, CAST(value as int) as value_configured, CAST(value_in_use as int) as value_in_use FROM sys.configurations WHERE name='Database Mail XPs'"

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):

        for rows in results:
            for row in rows:
                if 0 == row[1]:
                    self.result['level']  = 'GREEN'
                    self.result['output'] = 'Database Mail XPs is (%s) not enabled.' % (row[1])
                else:
                    self.result['level']  = 'RED'
                    self.result['output'] = 'Database Mail XPs is (%s) enabled.' % (row[1])

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
