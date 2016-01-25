class check_user_any_host():
    """
    check_user_any_host:
    User can connect from any host.
    """
    # References:

    TITLE    = 'Connect from Any Host'
    CATEGORY = 'User'
    TYPE     = 'sql'
    SQL         = "SELECT user, host FROM mysql.user WHERE host='%'"

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):
        output  = ''

        for rows in results:
            if len(rows) > 0:
                self.result['level'] = 'RED'
                for row in rows:
                    output += 'user: ' + str(row[0]) + ' host: ' + str(row[1]) + '\n'
            else:
                self.result['level']  = 'GREEN'
                output                = 'No users can connect from any host.'

            self.result['output'] = output

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
