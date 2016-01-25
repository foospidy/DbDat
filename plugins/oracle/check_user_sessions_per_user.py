class check_user_sessions_per_user():
    """
    check_user_sessions_per_user:
    The    SESSIONS_PER_USER (Number of sessions allowed) determines the maximum
    number of user sessions that are allowed to be open concurrently.
    """
    # References:
    # https://benchmarks.cisecurity.org/downloads/show-single/?file=oracle11gR2.210

    TITLE    = 'Sessions Per User'
    CATEGORY = 'User'
    TYPE     = 'sql'
    SQL         = "SELECT profile, resource_name, limit FROM sys.dba_profiles WHERE resource_name='SESSIONS_PER_USER' AND (limit='DEFAULT' OR limit='UNLIMITED' OR LIMIT>10)"

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
                    output += 'Sessions Per User for the ' + row[0] + ' profile is ' + row[2] + '\n'

        if 'GREEN' == self.result['level']:
            output = 'Sessions Per User is 10 or lessL.'

        self.result['output'] = output

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
