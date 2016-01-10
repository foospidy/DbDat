import helper

class check_configuration_nohttpinterface():
    """
    check_configuration_nohttpinterface:
    Mongodb by default provides a http interface running by default on port 28017 which
    provides the "home" status page. This interface is not recommended for production
    use and is best disabled. Use the "nohttpinterface" configuration setting to disable
    the http interface.
    """
    # References:
    # http://blog.mongodirector.com/10-tips-to-improve-your-mongodb-security/

    TITLE    = 'No HTTP Interface'
    CATEGORY = 'Configuration'
    TYPE     = 'configuration_file'
    SQL    	 = None # SQL not needed... because this is NoSQL.

    verbose = False
    skip	= False
    result  = {}

    def do_check(self, configuration_file):
        value = helper.get_config_value(configuration_file, 'nohttpinterface')

        if None == value:
            self.result['level']  = 'YELLOW'
            self.result['output'] = 'No HTTP Interface setting not found.'
        elif 'true' == value.lower():
            self.result['level']  = 'GREEN'
            self.result['output'] = 'No HTTP Interface is (%s) enabled.' % (value)
        else: 
            self.result['level']  = 'RED'
            self.result['output'] = 'No HTTP Interface is (%s) not enabled.' % (value)

        return self.result
	
    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)

        self.verbose = parent.verbose
