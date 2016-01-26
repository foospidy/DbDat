import helper

class check_configuration_ssl_weak_cert_validation():
    """
    check_configuration_ssl_weak_cert_validation:
    Disables the requirement for SSL certificate validation, that --sslCAFile 
    enables. With --sslWeakCertificateValidation, mongod or mongos will accept 
    connections if the client does not present a certificate when establishing 
    the connection.

    MongoDB versions under 2.6: check if "--sslWeakCertificateValidation" was passed as a command line argument.
    MongoDB versions 2.6 and above, check the net.ssl.weakCertificateValidation configuration option.
    """
    # References:
    # https://docs.mongodb.org/v2.4/reference/configuration-options/#cmdoption--sslWeakCertificateValidation
    # https://docs.mongodb.org/v2.6/reference/configuration-options/#net.ssl.weakCertificateValidation

    TITLE    = 'Weak Certificate Validation'
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
            option               = '--sslWeakCertificateValidation'
            weak_cert_validation = False

            try:
                dcurs  = self.db['admin']
                result = dcurs.command('getCmdLineOpts')

                if option in result['argv']:
                    weak_cert_validation = True

            except Exception as e:
                result['level']  = 'ORANGE'
                result['output'] = 'Error: %s' % (e)

            if weak_cert_validation:
                self.result['level']  = 'RED'
                self.result['output'] = '%s is enabled.' % (option)
            else:
                self.result['level']  = 'GREEN'
                self.result['output'] = '%s is not enabled.' % (option)

        else:
            option = 'net.ssl.weakCertificateValidation'
            value  = helper.get_yaml_config_value(configuration_file, option)

            if None == value:
                self.result['level']  = 'GREEN'
                self.result['output'] = '%s not found, not enabled.' % (option)
            elif False == value:
                self.result['level']  = 'GREEN'
                self.result['output'] = '%s is (%s) not enabled.' % (option, value)
            else:
                self.result['level']  = 'RED'
                self.result['output'] = '%s is (%s) enabled.' % (option, value)

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)

        self.verbose = parent.verbose
        self.db      = parent.db
