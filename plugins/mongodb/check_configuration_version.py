class check_configuration_version():
    """
    check_configuration_version:
    Determine current database version
    """
    # References:

    TITLE    = 'Version Check'
    CATEGORY = 'Information'
    TYPE     = 'nosql'
    SQL    	 = None # SQL not needed... because this is NoSQL.

    verbose = False
    skip	= False
    result  = {}
    db      = None

    def do_check(self):
        LATEST_VERSION = '3.2.0'
        version_number = self.db.server_info()['versionArray']
        string_version = self.db.server_info()['version']
        
        if version_number:
            latest = LATEST_VERSION.split('.')

            if int(version_number[0]) < int(latest[0]):
                self.result['level']  = 'RED'
                self.result['output'] = '%s very old version.' % (string_version)
                
            elif int(version_number[1]) < int(latest[1]):
                self.result['level']  = 'YELLOW'
                self.result['output'] = '%s old version.' % (string_version)
                
            elif int(version_number[2]) < int(latest[2]):
                self.result['level']  = 'YELLOW'
                self.result['output'] = '%s slightly old version.' % (string_version)
                
            else:
                self.result['level']  = 'GREEN'
                self.result['output'] = '%s recent version.' % (string_version)
        
        return self.result
	
    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
        self.db = parent.db
