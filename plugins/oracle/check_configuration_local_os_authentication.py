class check_configuration_local_os_authentication():
    """
    check_configuration_local_os_authentication
    If the os_authent_prefix is "" (Null), then the OS Authenticated accounts
    cannot log in using the password
    """
    # References:
    # http://www.dba-oracle.com/security/local_os_authentication.htm

    TITLE    = 'Local OS Authentication'
    CATEGORY = 'Configuration'
    TYPE     = 'sql'
    SQL         = "SELECT UPPER(value) FROM v$parameter WHERE UPPER(name)='OS_AUTHENT_PREFIX'"

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):

        for rows in results:
            for row in rows:
                if '' != str(row[0]):
                    self.result['level']  = 'RED'
                    self.result['output'] = 'OS authentication prefix is (%s) enabled. Set os_authent_prefix to null.' % (row[0])
                else:
                    self.result['level']  = 'GREEN'
                    self.result['output'] = 'OS authentication prefix is "(%s)" not enabled.' % (row[0])

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
