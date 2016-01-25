class check_privilege_proxy_users_connect():
    """
    check_privilege_proxy_users_connect:
    Do not grant privileges directly to proxy users.
    """
    # References:
    # https://benchmarks.cisecurity.org/downloads/show-single/?file=oracle11gR2.210

    TITLE    = 'Proxy Users CONNECT'
    CATEGORY = 'Privilege'
    TYPE     = 'sql'
    SQL         = "SELECT grantee, granted_role FROM dba_role_privs WHERE grantee IN (SELECT proxy FROM dba_proxies) AND granted_role NOT IN ('CONNECT')"

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):
        self.result['level']  = 'GREEN'
        output                = ''

        for rows in results:
            for row in rows:
                self.result['level'] = 'RED'
                output += 'Proxy user %s in %s\n' % (row[0], row[1])

        if 'GREEN' == self.result['level']:
            output = 'No proxy users with CONNECT found.'

        self.result['output'] = output

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
