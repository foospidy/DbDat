class check_user_password_verify_function():
    """
    check_user_password_verify_function:
    The    password_verify_function determines    password settings requirements when
    a user password is changed    at the SQL command prompt. This setting does not
    apply for users managed by the Oracle password file.
    """
    # References:
    # https://benchmarks.cisecurity.org/downloads/show-single/?file=oracle11gR2.210

    TITLE    = 'Password Verify Function'
    CATEGORY = 'User'
    TYPE     = 'sql'
    SQL         = "SELECT profile, resource_name, limit FROM sys.dba_profiles WHERE resource_name='PASSWORD_VERIFY_FUNCTION' AND (limit='DEFAULT' OR limit='NULL')"

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
                    output += 'Password Verify Function for the ' + row[0] + ' profile is ' + row[2] + '\n'

        if 'GREEN' == self.result['level']:
            output = 'Password Verify Function is not DEFAULT or NULL.'

        self.result['output'] = output

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
