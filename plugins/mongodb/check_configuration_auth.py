import helper

class check_configuration_auth():
    """
    check_configuration_auth:
    Authentication should be enabled.
    """
    # References:
    # http://blog.mongodirector.com/10-tips-to-improve-your-mongodb-security/

    TITLE    = 'Enable Auth'
    CATEGORY = 'Configuration'
    TYPE     = 'configuration_file'
    SQL    	 = None

    verbose = False
    skip	= False
    result  = {}

    def do_check(self, configuration_file):
        value = helper.get_config_value(configuration_file, 'auth')

        if None == value:
            self.result['level']  = 'YELLOW'
            self.result['output'] = 'MongoDB Authentication setting not found.'
        elif 'true' == value.lower():
            self.result['level']  = 'GREEN'
            self.result['output'] = 'MongoDB Authentication is (%s) enabled.' % (value)
        else: 
            self.result['level']  = 'RED'
            self.result['output'] = 'MongoDB Authentication is (%s) not enabled.' % (value)

        return self.result
	
    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)

        self.verbose = parent.verbose
