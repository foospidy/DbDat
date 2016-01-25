class check_configuration_sec_return_server_release_banner():
    """
    check_configuration_sec_return_server_release_banner:
    The information about patch/update release number provides information about
    the exact patch/update release that is currently running on the database.
    """
    # References:
    # https://benchmarks.cisecurity.org/downloads/show-single/?file=oracle11gR2.210

    TITLE    = 'Return Server Release Banner'
    CATEGORY = 'Configuration'
    TYPE     = 'sql'
    SQL         = "SELECT UPPER(value) FROM v$parameter WHERE UPPER(name)='SEC_RETURN_SERVER_RELEASE_BANNER'"

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):

        for rows in results:
            for row in rows:
                if 'FALSE' != row[0]:
                    self.result['level']  = 'YELLOW'
                    self.result['output'] = 'SEC_RETURN_SERVER_RELEASE_BANNER is (%s) enabled.' % (row[0])
                else:
                    self.result['level']  = 'GREEN'
                    self.result['output'] = 'SEC_RETURN_SERVER_RELEASE_BANNER is (%s) not enabled.' % (row[0])

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
