class check_configuration_fifteenth_spare_parameter():
    """
    check_configuration_fifteenth_spare_parameter
    Ensure _fifteenth_spare_parameter is set to 'all'.
    The _fifteenth_spare_parameter determines whether the oradebug facility 
    has been disabled or not.
    """
    # References:
    # http://www.davidlitchfield.com/AddendumtotheOracle12cCISGuidelines.pdf
    # http://blog.red-database-security.com/2013/09/13/fix-for-oradebug-disable-auditing- available-11-2-0-3/

    TITLE    = 'Fifteenth Spare Parameter'
    CATEGORY = 'Configuration'
    TYPE     = 'sql'
    SQL      = "SELECT c.ksppstvl FROM x$ksppi a, x$ksppsv c WHERE a.indx = c.indx AND a.ksppinm = '_fifteenth_spare_parameter'"

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):

        for rows in results:
            for row in rows:
                if 'all' != row[0]:
                    self.result['level']  = 'RED'
                    self.result['output'] = 'Fifteenth Spare Parameter is (%s).' % (row[0])
                else:
                    self.result['level']  = 'GREEN'
                    self.result['output'] = 'Fifteenth Spare Parameter is (%s).' % (row[0])

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
