import helper

class check_information_bind_ip():
    """
    check_information_bind_ip:
    If your system has multiple network interfaces you can use the "bind_ip" option
    to restrict your mongodb server to listen only on the interfaces that are
    relevant. By default mongodb will bind to all the interfaces.
    """
    # References:
    # http://blog.mongodirector.com/10-tips-to-improve-your-mongodb-security/

    TITLE    = 'Bind IP'
    CATEGORY = 'Information'
    TYPE     = 'configuration_file'
    SQL    	 = None

    verbose = False
    skip	= False
    result  = {}
	
    def do_check(self, configuration_file):
        try:
            value = helper.get_config_value(configuration_file, 'bind_ip')

            self.result['level']  = 'GREEN'
            self.result['output'] = 'Bind IP is (%s) enabled.' % (value)

        except ConfigParser.NoOptionError as e:
            self.result['level']  = 'YELLOW'
            self.result['output'] = 'Bind IP setting not found.'

        return self.result
	
    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)

        self.verbose = parent.verbose
