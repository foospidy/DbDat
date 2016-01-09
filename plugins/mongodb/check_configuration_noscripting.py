import helper

class check_configuration_noscripting():
    """
    check_configuration_noscripting:
    MongoDB supports the execution of JavaScript code for certain server-side operations: 
    mapReduce, group, eval, and $where. If you do not use these operations, disable server-side
    scripting by using the --noscripting option on the command line.
    """
    # References:
    # https://docs.mongodb.org/v2.6/MongoDB-security-guide-v2.6.pdf

    TITLE    = 'No Scripting'
    CATEGORY = 'Configuration'
    TYPE     = 'configuration_file'
    SQL    	 = None

    verbose = False
    skip	= False
    result  = {}

    def do_check(self, configuration_file):
        value = helper.get_config_value(configuration_file, 'noscripting')

        if None == value:
            self.result['level']  = 'RED'
            self.result['output'] = 'noscripting is (not found) not enabled.'
        elif 'true' != value.lower():
            self.result['level']  = 'GREEN'
            self.result['output'] = 'noscripting is (%s) enabled.' % (value)
        else: 
            self.result['level']  = 'RED'
            self.result['output'] = 'noscripting is (%s) not enabled.' % (value)

        return self.result
	
    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)

        self.verbose = parent.verbose
