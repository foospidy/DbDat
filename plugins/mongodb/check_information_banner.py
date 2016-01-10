class check_information_banner():
    """
    check_configuration_version:
    Determine current database version
    """
    # References:

    TITLE    = 'Server Info'
    CATEGORY = 'Information'
    TYPE     = 'nosql'
    SQL    	 = None # SQL not needed... because this is NoSQL.

    verbose = False
    skip	= False
    result  = {}
    
    db      = None

    def do_check(self):
        self.result['level'] = 'GREEN'
        output               = ''

        info = self.db.server_info()
        for name, value in info.items():
            output += '%s = %s\n' % (name, value)
        
        self.result['output'] = output
        
        return self.result
	
    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
        self.db = parent.db
