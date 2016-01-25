class check_user_dba_users_password():
    """
    check_user_dba_users_password:
    The    password='EXTERNAL' setting determines whether or not a    user can be authenticated
    by a remote    OS to allow    access to the database with    full authorization.
    """
    # References:
    # https://benchmarks.cisecurity.org/downloads/show-single/?file=oracle11gR2.210

    TITLE    = 'DBA Users Password'
    CATEGORY = 'User'
    TYPE     = 'sql'
    SQL         = "SELECT username FROM sys.dba_users WHERE password='EXTERNAL'"

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):
        self.result['level']  = 'GREEN'
        output                = ''

        for rows in results:
            for row in rows:
                if 'UNLIMITED' == row[2]:
                    self.result['level'] = 'RED'
                    output += 'DBA Users Password set to EXTERNAL for ' + row[0] + '\n'

        if 'GREEN' == self.result['level']:
            output = 'NO DBA Users Passwords set to EXTERNAL.'

        self.result['output'] = output

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
