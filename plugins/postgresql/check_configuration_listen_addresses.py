import helper

class check_configuration_listen_addresses():
    """
    check_configuration_listen_addresses
    """
    # References:
    # http://www.postgresql.org/docs/9.3/static/auth-pg-hba-conf.html

    TITLE    = 'Listen Addresses'
    CATEGORY = 'Configuration'
    TYPE     = 'configuration_file'
    SQL         = None

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, configuration_file):
        addresses            = None
        output               = ''
        self.result['level'] = 'GREEN'

        addresses = helper.get_config_value(configuration_file, 'listen_addresses')

        if not addresses:
            # if option not found then postgresql defaults to localhost
            addresses = 'localhost'

        if 'localhost' != addresses:
            self.result['level'] = 'YELLOW'
            output               = 'Database listening is not localhost only (' + addresses + ')'

        self.result['output'] = output

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)

        self.verbose = parent.verbose
