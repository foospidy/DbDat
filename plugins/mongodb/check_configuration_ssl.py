import helper

class check_configuration_ssl():
    """
    check_configuration_ssl:
    If you don't use SSL your data is traveling between your Mongo client and Mongo 
    server unencrypted and is susceptible to eavesdropping, tampering and "man in 
    the middle" attacks. This is especially important if you are connecting to your 
    Mongodb server over unsecure networks like the internet.
    """
    # References:
    # http://blog.mongodirector.com/10-tips-to-improve-your-mongodb-security/
    # https://docs.mongodb.org/v2.4/reference/configuration-options/#ssl-options
    # https://docs.mongodb.org/v2.6/tutorial/configure-ssl/
    # https://docs.mongodb.org/v2.6/reference/configuration-options/#net-ssl-options

    TITLE    = 'Enable SSL'
    CATEGORY = 'Configuration'
    TYPE     = 'configuration_file'
    SQL    	 = None # SQL not needed... because this is NoSQL.

    verbose = False
    skip	= False
    result  = {}

    def do_check(self, configuration_file):
        value = helper.get_config_value(configuration_file, 'sslPEMKeyFile')

        if None == value:
            self.result['level']  = 'RED'
            self.result['output'] = 'SSL is (not found) not enabled.'
        elif '' != value.lower():
            self.result['level']  = 'GREEN'
            self.result['output'] = 'SSL is (%s) enabled.' % (value)
        else: 
            self.result['level']  = 'RED'
            self.result['output'] = 'SSL is (%s) not enabled.' % (value)

        return self.result
	
    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)

        self.verbose = parent.verbose
