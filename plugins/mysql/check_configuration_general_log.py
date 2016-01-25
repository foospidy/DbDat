import ConfigParser

class check_configuration_general_log():
    """
    check_configuration_general_log
    """
    # References:
    # https://www.percona.com/blog/2012/12/28/auditing-login-attempts-in-mysql/

    TITLE    = 'Check General Log'
    CATEGORY = 'Configuration'
    TYPE     = 'configuration_file'
    SQL         = None

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, configuration_file):
        configuration = ConfigParser.ConfigParser()

        try:
            configuration.read(configuration_file)

        except ConfigParser.ParsingError as e:
            if self.verbose:
                print('Ignoring parsing errors:\n' + str(e))

        try:
            general_log_file = configuration.get('mysqld', 'general_log_file')

        except ConfigParser.NoOptionError as e:
            self.result['level']  = 'YELLOW'
            self.result['output'] = 'General log file not enabled.'

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)

        self.verbose = parent.verbose
