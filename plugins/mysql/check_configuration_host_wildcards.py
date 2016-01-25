class check_configuration_host_wildcards():
    """
    check_configuration_host_wildcards
    Wildcard hosts should not be used.
    """
    # References:

    TITLE    = 'Wildcard Hosts'
    CATEGORY = 'Configuration'
    TYPE     = 'sql'
    SQL         = "SELECT user, host FROM mysql.user WHERE host LIKE '%\%%'"

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):
        self.result['level']  = 'GREEN'
        output                = ''

        for rows in results:
            for row in rows:
                self.result['level'] = 'RED'
                output += 'user: ' + str(row[0]) + ' host: ' + str(row[1]) + '\n'

        if 'GREEN' == self.result['level']:
            output = 'No wildcard hosts found.'

        self.result['output'] = output

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
