class check_configuration_sec_case_sensitive_logon():
    """
    check_configuration_sec_case_sensitive_logon:
    The SEC_CASE_SENSITIVE_LOGON information determines whether or not
    case-sensitivity is required for passwords during login.
    """
    # References:
    # https://benchmarks.cisecurity.org/downloads/show-single/?file=oracle11gR2.210

    TITLE    = 'Case Sensitive Logon'
    CATEGORY = 'Configuration'
    TYPE     = 'sql'
    SQL         = "SELECT UPPER(value) FROM v$parameter WHERE UPPER(name)='SEC_CASE_SENSITIVE_LOGON'"

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):
        self.result['level']  = 'GREEN'
        self.result['output'] = 'Case Sensitive Logon is enabled.'

        for rows in results:
            for row in rows:
                if 'TRUE' != row[0]:
                    self.result['level']  = 'RED'
                    self.result['output'] = 'Case Sensitive Logon is (%s) not enabled.' % (row[0])

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
