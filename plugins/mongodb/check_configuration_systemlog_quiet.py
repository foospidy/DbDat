import helper
from distutils.version import LooseVersion

class check_configuration_systemlog_quiet():
    """
    check_configuration_systemlog_quiet:
    Runs the mongos or mongod in a quiet mode that attempts to limit the amount
    of output. This option is not recommended for production systems as it may 
    make tracking problems during particular connections much more difficult.

    MongoDB versions 2.6.4 and above, check the systemLog.quiet configuration option.
    """
    # References:
    # https://docs.mongodb.org/v2.6/reference/configuration-options/#systemLog.quiet

    TITLE    = 'System Log Quiet'
    CATEGORY = 'Configuration'
    TYPE     = 'configuration_file'
    SQL         = None # SQL not needed... because this is NoSQL.

    verbose = False
    skip    = False
    result  = {}

    db      = None

    def do_check(self, configuration_file):
        option         = None
        version_number = self.db.server_info()['version']
        
        if LooseVersion(version_number) >= LooseVersion("2.6"):
            option = 'systemLog.quiet'
            value  = helper.get_yaml_config_value(configuration_file, option)

            if None == value:
                self.result['level']  = 'GREEN'
                self.result['output'] = '%s not found, not enabled.' % (option)
            elif False == value:
                self.result['level']  = 'GREEN'
                self.result['output'] = '%s is (%s) not enabled.' % (option, value)
            else:
                self.result['level']  = 'YELLOW'
                self.result['output'] = '%s is (%s) enabled.' % (option, value)

        else:
            self.result['level']  = 'GRAY'
            self.result['output'] = 'This check does not apply to MongoDB versions below 2.6.'

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)

        self.verbose = parent.verbose
        self.db      = parent.db
