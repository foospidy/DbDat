class check_configuration_trustworthy_database():
    """
    check_configuration_trustworthy_database:
    The TRUSTWORTHY option allows database objects to access objects in other
    database under certain circumstances.
    """
    # References:
    # https://benchmarks.cisecurity.org/downloads/show-single/index.cfm?file=sql2012DB.120

    TITLE    = 'Trustworthy Database'
    CATEGORY = 'Configuration'
    TYPE     = 'sql'
    SQL         = "SELECT name FROM sys.databases WHERE is_trustworthy_on=1 AND name != 'msdb' AND state=0"

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):
        output                = ''
        self.result['level']  = 'GREEN'

        for rows in results:
            for row in rows:
                self.result['level'] = 'RED'
                output += 'Database (%s) with trustworthy enabled.\n' % (row[0])

        if 'GREEN' == self.result['level']:
            output = 'No databases found with trustworthy enabled.'

        self.result['output'] = output

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
