import helper

class check_configuration_rest_interface():
    """
    check_configuration_rest_interface:
    he monogdb REST interface is not recommended for production. It does not support
    any authentication. It is turned off by default. If you have turned it on using
    the "rest" configuration option you should turn it off for production systems.
    """
    # References:
    # http://blog.mongodirector.com/10-tips-to-improve-your-mongodb-security/

    TITLE    = 'REST Interface'
    CATEGORY = 'Configuration'
    TYPE     = 'configuration_file'
    SQL    	 = None # SQL not needed... because this is NoSQL.

    verbose = False
    skip	= False
    result  = {}
	
    def do_check(self, configuration_file):
        value = helper.get_config_value(configuration_file, 'rest')

        if None == value:
            self.result['level']  = 'YELLOW'
            self.result['output'] = 'HTTP Status Interface setting not found.'
        elif 'false' == value.lower():
            self.result['level']  = 'GREEN'
            self.result['output'] = 'REST Interface is (%s) enabled.' % (value)
        else: 
            self.result['level']  = 'RED'
            self.result['output'] = 'REST Interface is (%s) not enabled.' % (value)
            
        return self.result
	
    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)

        self.verbose = parent.verbose
