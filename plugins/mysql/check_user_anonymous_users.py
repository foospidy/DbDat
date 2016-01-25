class check_user_anonymous_users():
    """
    check_user_anonymous_users:
    Do anonymous users exist.
    """
    # References:

    TITLE    = 'Anonymous Users'
    CATEGORY = 'User'
    TYPE     = 'sql'
    SQL      = "SELECT * FROM mysql.user WHERE user=''"

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):
        output  = ''

        for rows in results:
            if len(rows) > 0:
                self.result['level'] = 'RED'
                for row in rows:
                    output += row[0] + "\n"
            else:
                self.result['level']  = 'GREEN'
                output                = 'No anonymous users found.'

            self.result['output'] = output

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
