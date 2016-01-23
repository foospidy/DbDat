import helper

class check_configuration_keyfile():
    """
    check_configuration_keyfile:
    Specify a shared key file to enable communication between MongoDB instances in a
    replica set.
    
    MongoDB versions under 2.6: check the "keyFile" configuration option
    MongoDB versions 2.6 and above, check the security.keyFile option
    """
    # References:
    # http://blog.mongodirector.com/10-tips-to-improve-your-mongodb-security/
	# https://docs.mongodb.org/v2.4/reference/configuration-options/#keyFile
	# https://docs.mongodb.org/v2.6/reference/configuration-options/#security.keyFile

    TITLE    = 'Key File for Replica Set'
    CATEGORY = 'Configuration'
    TYPE     = 'configuration_file'
    SQL    	 = None # SQL not needed... because this is NoSQL.

    verbose = False
    skip	= False
    result  = {}

    def do_check(self, configuration_file):
        option         = None
        version_number = self.db.server_info()['versionArray']

        if version_number[0] <= 2 and version_number[1] < 6:
            option = 'keyFile'
            value  = helper.get_config_value(configuration_file, option)
        
            if None == value:
                self.result['level']  = 'YELLOW'
                self.result['output'] = 'keyFile setting not found.'
            elif '' != value.lower():
                self.result['level']  = 'GREEN'
                self.result['output'] = 'keyFile is (%s) enabled.' % (value)
            else: 
                self.result['level']  = 'YELLOW'
                self.result['output'] = 'keyFile is (%s) not enabled.' % (value)
        else:
            option = 'security.keyFile'
            value  = helper.get_yaml_config_value(configuration_file, option)

            if None == value:
                self.result['level']  = 'YELLOW'
                self.result['output'] = '%s is (not found) not enabled.' % (option)
            elif '' == str(value):
                self.result['level']  = 'YELLOW'
                self.result['output'] = '%s is (%s) not enabled.' % (option, value)
            else: 
                self.result['level']  = 'GREEN'
                self.result['output'] = '%s is (%s) enabled.' % (option, value)
            
        return self.result
	
    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)

        self.verbose = parent.verbose
        self.db      = parent.db
