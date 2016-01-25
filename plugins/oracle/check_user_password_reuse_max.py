class check_user_password_reuse_max():
    """
    check_user_password_reuse_max:
    The    password_reuse_max setting determines how many different passwords must
    be used before the    user is allowed    to reuse a prior password.
    """
    # References:
    # https://benchmarks.cisecurity.org/downloads/show-single/?file=oracle11gR2.210

    TITLE    = 'Password Reuse Max'
    CATEGORY = 'User'
    TYPE     = 'sql'
    SQL         = "SELECT profile, resource_name, limit FROM sys.dba_profiles WHERE resource_name='PASSWORD_REUSE_MAX' AND (limit='DEFAULT' OR limit='UNLIMITED' OR limit<20)"

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
                    output += 'Password Reuse Max for the ' + row[0] + ' profile is ' + row[2] + '\n'

        if 'GREEN' == self.result['level']:
            output = 'Password Reuse Max is at least 20.'

        self.result['output'] = output

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
