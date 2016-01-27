import helper

class check_configuration_ssl_fips_mode():
    """
    check_configuration_ssl_fips_mode:
    When specified, mongos will use the FIPS mode of the installed OpenSSL 
    library. Your system must have a FIPS compliant OpenSSL library to use 
    --sslFIPSMode.
    
    MongoDB versions under 2.6: check if "--sslFIPSMode" was passed as a command line argument.
    MongoDB versions 2.6 and above, check the net.ssl.FIPSMode configuration option.
    """
    # References:
    # https://docs.mongodb.org/v2.4/reference/program/mongos/#cmdoption--sslFIPSMode
    # https://docs.mongodb.org/v2.6/reference/configuration-options/#net.ssl.FIPSMode
    # https://jira.mongodb.org/browse/SERVER-7648
    # https://jira.mongodb.org/browse/SERVER-8459

    TITLE    = 'SSL FIPS Mode'
    CATEGORY = 'Configuration'
    TYPE     = 'configuration_file'
    SQL         = None # SQL not needed... because this is NoSQL.

    verbose = False
    skip    = False
    result  = {}

    db      = None

    def do_check(self, configuration_file):
        option         = None
        version_number = self.db.server_info()['versionArray']

        if version_number[0] <= 2 and version_number[1] < 6:
            option    = '--sslFIPSMode'
            fips_mode = False

            try:
                dcurs  = self.db['admin']
                result = dcurs.command('getCmdLineOpts')

                if option in result['argv']:
                    fips_mode = True

            except Exception as e:
                result['level']  = 'ORANGE'
                result['output'] = 'Error: %s' % (e)

            if fips_mode:
                self.result['level']  = 'GREEN'
                self.result['output'] = '%s is enabled.' % (option)
            else:
                self.result['level']  = 'YELLOW'
                self.result['output'] = '%s is not enabled.' % (option)

        else:
            option = 'net.ssl.FIPSMode'
            value  = helper.get_yaml_config_value(configuration_file, option)

            if None == value:
                self.result['level']  = 'YELLOW'
                self.result['output'] = '%s not found, not enabled.' % (option)
            elif False == value:
                self.result['level']  = 'YELLOW'
                self.result['output'] = '%s is (%s) not enabled.' % (option, value)
            else:
                self.result['level']  = 'GREEN'
                self.result['output'] = '%s is (%s) enabled.' % (option, value)

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)

        self.verbose = parent.verbose
        self.db      = parent.db
