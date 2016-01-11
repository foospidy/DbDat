class check_configuration_log_level():
    """
    check_configuration_log_level:
    Ensure the log level is approrpiate for your environment. Typically debug 
    level should not be enabled in production. With debug level enabled user
    passowrds may be logged in plain text.
    """
    # References:
    # 

    TITLE    = 'Debug Log Level'
    CATEGORY = 'Configuration'
    TYPE     = 'nosql'
    SQL    	 = None # SQL not needed... because this is NoSQL.

    verbose = False
    skip	= False
    result  = {}
    db      = None

    def do_check(self):
        value = self.db.config()['log']['level']
        
        if 'debug' == value:
            self.result['level']  = 'RED'
            self.result['output'] = 'Log level is (%s).' % (value)
        elif 'info' == value:
            self.result['level']  = 'GREEN'
            self.result['output'] = 'Log level is (%s).' % (value)
        else:
            self.result['level']  = 'YELLOW'
            self.result['output'] = 'Log level is (%s).' % (value)
        
        return self.result
	
    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
        self.db = parent.db
