class check_user_root_name():
    """
    check_user_root_name:
    Change the default name of administrator's account name (root).
    """
    # References:

    TITLE    = 'Root Account Name'
    CATEGORY = 'User'
    TYPE     = 'sql'
    SQL         = "SELECT user, host FROM mysql.user WHERE user = 'root'"

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
                output                = 'No root account name found.'

            self.result['output'] = output

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
