from pymongo import MongoClient
import helper

class check_configuration_localhost_auth_bypass():
    """
    check_configuration_localhost_auth_bypass:
    The localhost exception allows you to enable authorization before creating
    the first user in the system. When active, the localhost exception allows 
    all connections from the localhost interface to have full access to that 
    instance. The exception applies only when there are no users created in the
    MongoDB instance.
    """
    # References:
    # https://docs.mongodb.org/v2.6/core/authentication/#localhost-exception
    # https://docs.mongodb.org/v2.6/reference/parameters/#param.enableLocalhostAuthBypass

    TITLE    = 'Localhost Auth Bypass'
    CATEGORY = 'Configuration'
    TYPE     = 'configuration_file'
    SQL    	 = None # SQL not needed... because this is NoSQL.

    verbose = False
    skip	= False
    result  = {}
    
    db      = None

    def do_check(self, configuration_file):
        option         = None
        version_number = self.db.server_info()['versionArray']
        
        if version_number[0] <= 2 and version_number[1] < 6:
            option = 'enableLocalhostAuthBypass'
            
            # setParameter can't be retrived using helper.get_config_value(), so do this...
            with open(configuration_file, 'r') as config:
                for line in config:
                    values = line.split('=')
                    if 'setParameter' == values[0].strip():
                        if option == values[1].strip():
                            value = values[2].strip()

            if None == value:
                self.result['level']  = 'RED'
                self.result['output'] = '%s is (not found) not enabled.' % (option)
            elif 'false' == value.lower():
                self.result['level']  = 'GREEN'
                self.result['output'] = '%s is (%s) not enabled.' % (option, value)
            else: 
                self.result['level']  = 'RED'
                self.result['output'] = '%s is (%s) enabled.' % (option, value)
            
        else:
            option = 'setParameter.enableLocalhostAuthBypass'
            value  = helper.get_yaml_config_value(configuration_file, option)
            
            if None == value:
                self.result['level']  = 'RED'
                self.result['output'] = '%s is (not found) enabled.' % (option)
            elif False == value:
                self.result['level']  = 'GREEN'
                self.result['output'] = '%s is (%s) not enabled.' % (option, value)
            else: 
                self.result['level']  = 'RED'
                self.result['output'] = '%s is (%s) enabled.' % (option, value)

        return self.result
	
    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
        
        # parent connection is authenticated so create a new unauthenticated connection
        self.db = MongoClient(parent.dbhost, int(parent.dbport))
