import helper

class check_configuration_keyfile():
    """
    check_configuration_keyfile:
    Specify a shared key file to enable communication between MongoDB instances in a
    replica set.
    """
    # References:
    # http://blog.mongodirector.com/10-tips-to-improve-your-mongodb-security/

    TITLE    = 'Key File for Replica Set'
    CATEGORY = 'Configuration'
    TYPE     = 'configuration_file'
    SQL    	 = None # SQL not needed... because this is NoSQL.

    verbose = False
    skip	= False
    result  = {}

    def do_check(self, configuration_file):
        value = helper.get_config_value(configuration_file, 'keyFile')
        
        if None == value:
            self.result['level']  = 'YELLOW'
            self.result['output'] = 'keyFile setting not found.'
        elif '' != value.lower():
            self.result['level']  = 'GREEN'
            self.result['output'] = 'keyFile is (%s) enabled.' % (value)
        else: 
            self.result['level']  = 'YELLOW'
            self.result['output'] = 'keyFile is (%s) not enabled.' % (value)

        return self.result
	
    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)

        self.verbose = parent.verbose
