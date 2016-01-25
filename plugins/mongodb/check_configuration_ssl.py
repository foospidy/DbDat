import helper

class check_configuration_ssl():
    """
    check_configuration_ssl:
    If you don't use SSL your data is traveling between your Mongo client and Mongo
    server unencrypted and is susceptible to eavesdropping, tampering and "man in
    the middle" attacks. This is especially important if you are connecting to your
    Mongodb server over unsecure networks like the internet.

    MongoDB versions under 2.6: check if the "sslPEMKeyFile" configuration option is set.
    MongoDB versions 2.6 and above, check the net.ssl.mode option.
    """
    # References:
    # http://blog.mongodirector.com/10-tips-to-improve-your-mongodb-security/
    # https://docs.mongodb.org/v2.4/reference/configuration-options/#ssl-options
    # https://docs.mongodb.org/v2.6/tutorial/configure-ssl/
    # https://docs.mongodb.org/v2.6/reference/configuration-options/#net-ssl-options

    TITLE    = 'Enable SSL'
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
            option              = 'sslPEMKeyFile'
            value               = helper.get_config_value(configuration_file, option)
            ssl_on_normal_ports = False

            if version_number[0] >= 2 and version_number[1] >= 2:
                try:
                    dcurs  = self.db['admin']
                    result = dcurs.command('getCmdLineOpts')

                    if '--sslOnNormalPorts' in result['argv']:
                        ssl_on_normal_ports = True

                except Exception as e:
                    # this will actually be a silent exception values below will be overwritten
                    # the exception is here so execution doesn't break if something goes wrong
                    result['level']  = 'ORANGE'
                    result['output'] = 'Error: %s' % (e)

            if None == value:
                self.result['level']  = 'RED'
                self.result['output'] = '%s is not set, SSL is not enabled.' % (option)

                if ssl_on_normal_ports:
                    self.result['level']  = 'GREEN'
                    self.result['output'] = 'Command line option --sslOnNormalPorts set, SSL is enabled.'

            elif '' != value:
                self.result['level']  = 'GREEN'
                self.result['output'] = 'SSL is (%s: %s) enabled.' % (option, value)
            else:
                self.result['level']  = 'RED'
                self.result['output'] = 'SSL is (%s: %s) not enabled.' % (option, value)

        else:
            option = 'net.ssl.mode'
            value  = helper.get_yaml_config_value(configuration_file, option)

            if None == value:
                self.result['level']  = 'RED'
                self.result['output'] = 'SSL is (%s not found) not enabled.' % (option)
            elif 'requireSSL' == value:
                self.result['level']  = 'GREEN'
                self.result['output'] = 'SSL is (%s: %s) is required.' % (option, value)
            elif 'preferSSL' == value:
                self.result['level']  = 'YELLOW'
                self.result['output'] = 'SSL is (%s: %s) is prefered, but not required.' % (option, value)
            elif 'allowSSL' == value:
                self.result['level']  = 'YELLOW'
                self.result['output'] = 'SSL is (%s: %s) is allowed, but not required.' % (option, value)
            else:
                self.result['level']  = 'RED'
                self.result['output'] = 'SSL is (%s: %s) not enabled.' % (option, value)

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)

        self.verbose = parent.verbose
        self.db      = parent.db
