import helper

class check_configuration_noauth():
    """
    check_configuration_noauth:
    This will explicitly disable authentication. This setting applies to MondoDB versions below 2.6.
    """
    # References:
    # https://docs.mongodb.org/v2.4/reference/configuration-options/#noauth

    TITLE    = 'No Authentication'
    CATEGORY = 'Configuration'
    TYPE     = 'configuration_file'
    SQL      = None # SQL not needed... because this is NoSQL.

    verbose = False
    skip        = False
    result  = {}

    db      = None

    def do_check(self, configuration_file):
        option         = None
        version_number = self.db.server_info()['versionArray']

        if version_number[0] <= 2 and version_number[1] < 6:
            option = 'noauth'
            value = helper.get_config_value(configuration_file, option)

            if None == value:
                self.result['level']  = 'YELLOW'
                self.result['output'] = '%s setting not found. The default value is "true", ensure the "auth" option is enabled.' % (option)
            elif 'true' == value.lower():
                self.result['level']  = 'RED'
                self.result['output'] = '%s is (%s) enabled.' % (option, value)
            else:
                self.result['level']  = 'GREEN'
                self.result['output'] = '%s is (%s) not enabled.' % (option, value)

        else:
            self.result['level']  = 'GRAY'
            self.result['output'] = 'This check does not apply to MongoDB versions 2.6 and above.'

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)

        # db is needed to get version info
        self.db      = parent.db
        self.verbose = parent.verbose
