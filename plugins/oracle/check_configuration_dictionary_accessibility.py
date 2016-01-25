class check_configuration_dictionary_accessibility():
    """
    check_configuration_dictionary_accessibility
    Implement data dictionary protection to prevent users who have the ANY
    system privilege from using it on the data dictionary.
    """
    # References:
    # http://docs.oracle.com/cd/B19306_01/network.102/b14266/checklis.htm

    TITLE    = 'Dictionary Protection'
    CATEGORY = 'Configuration'
    TYPE     = 'sql'
    SQL         = "SELECT UPPER(value) FROM v$parameter WHERE UPPER(name)='O7_DICTIONARY_ACCESSIBILITY'"

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):

        for rows in results:
            for row in rows:
                if 'TRUE' == row[0]:
                    self.result['level']  = 'RED'
                    self.result['output'] = 'Dictionary accessibility is (%s), protection not enabled.' % (row[0])
                else:
                    self.result['level']  = 'GREEN'
                    self.result['output'] = 'Dictionary accessibility is (%s), protection enabled.' % (row[0])

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
