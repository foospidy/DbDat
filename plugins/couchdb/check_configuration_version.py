class check_configuration_version():
    """
    check_configuration_version:
    Determine current database version
    """
    # References:

    TITLE    = 'Version Check'
    CATEGORY = 'Configuration'
    TYPE     = 'nosql'
    SQL         = None # SQL not needed... because this is NoSQL.

    verbose = False
    skip    = False
    result  = {}
    db      = None

    def do_check(self):
        LATEST_VERSION = '1.6.1'
        version_number = self.db.version()

        if version_number:
            latest = LATEST_VERSION.split('.')
            thisdb = version_number.split('.')

            if int(thisdb[0]) < int(latest[0]):
                self.result['level']  = 'RED'
                self.result['output'] = '%s very old version.' % (version_number)

            elif int(thisdb[1]) < int(latest[1]):
                self.result['level']  = 'YELLOW'
                self.result['output'] = '%s old version.' % (version_number)

            elif int(thisdb[2]) < int(latest[2]):
                self.result['level']  = 'YELLOW'
                self.result['output'] = '%s slightly old version.' % (version_number)

            else:
                self.result['level']  = 'GREEN'
                self.result['output'] = '%s recent version.' % (version_number)

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
        self.db = parent.db
