class check_privilege_stale_users():
    """
    check_privilege_stale_users:
    Possible stale accounts. Account exists in msyql.db but not in mysql.user.
    """
    # References:

    TITLE    = 'Stale User Privilege'
    CATEGORY = 'Privilege'
    TYPE     = 'sql'
    SQL         = "SELECT user, host FROM mysql.db WHERE user NOT IN (SELECT user FROM mysql.user)"

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):
        self.result['level']  = 'GREEN'
        output                = ''

        for rows in results:
            for row in rows:
                self.result['level'] = 'RED'
                output += 'user: ' + str(r[0]) + ' host: ' + str(r[1]) + '\n'

        if 'GREEN' == self.result['level']:
            output = 'No stale privileges found.'

        self.result['output'] = output

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
