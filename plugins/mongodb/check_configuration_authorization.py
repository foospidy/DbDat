import helper
from distutils.version import LooseVersion

class check_configuration_authorization():
    """
    check_configuration_authorization:
    Enables Role-Based Access Control (RBAC) to govern each user's access to
    database resources and operations.

    MongoDB versions 2.6.4 and above, check the security.authorization configuration option.
    """
    # References:
    # https://docs.mongodb.org/v2.6/reference/configuration-options/#security.authorization

    TITLE    = 'Authorization'
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
            option = 'security.authorization'
            value  = helper.get_yaml_config_value(configuration_file, option)

            if None == value:
                self.result['level']  = 'RED'
                self.result['output'] = '%s not found, not enabled.' % (option)
            elif 'enabled' == value:
                self.result['level']  = 'GREEN'
                self.result['output'] = '%s is (%s) enabled.' % (option, value)
            else:
                self.result['level']  = 'RED'
                self.result['output'] = '%s is (%s) not enabled.' % (option, value)

        else:
            self.result['level']  = 'GRAY'
            self.result['output'] = 'This check does not apply to MongoDB versions below 2.6.'

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)

        self.verbose = parent.verbose
        self.db      = parent.db
