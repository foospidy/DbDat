import helper

class check_user_users_with_defpwd():
    """
    check_user_users_with_defpwd
    Users with default passwords.
    """
    # References:
    # http://docs.oracle.com/cd/B28359_01/server.111/b28320/statviews_5074.htm
    # https://www.sans.org/reading-room/whitepapers/analyst/oracle-database-security-secure-34885

    TITLE    = 'Users With Default Passowrds'
    CATEGORY = 'User'
    TYPE     = 'sql'
    SQL         = 'SELECT username FROM dba_users_with_defpwd'

    verbose = False
    skip    = False
    result  = {}

    dbversion = None

    def do_check(self, *results):
        output               = ''
        self.result['level'] = 'GREEN'

        if self.dbversion >= 11:
            for rows in results:
                for row in rows:
                    self.result['level'] = 'RED'
                    output += row[0] + '\n'

            self.result['output'] = output
        else:
            self.result['level'] = 'GRAY'
            output = 'This check only applies to Oracle versions 11 and above.'

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)

        self.dbversion = helper.get_version(parent.dbcurs)
