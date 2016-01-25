import ConfigParser
import StringIO
import os


def get_config_value(configuration_file, option, verbose=False):
    # mongodb config files do not have sections, so inject a dummy section
    # see: https://stackoverflow.com/questions/2819696/parsing-properties-file-in-python/
    config = StringIO.StringIO()
    config.write('[dbdat]\n')
    config.write(open(configuration_file).read())
    config.seek(0, os.SEEK_SET)

    value = None

    try:
        configuration = ConfigParser.ConfigParser()
        configuration.readfp(config)

    except ConfigParser.ParsingError as e:
        if verbose:
            print('Ignoring parsing errors:\n' + str(e))

    try:
        value = configuration.get('dbdat', option)

        # clean up required
        value = value.split()[0]
        value = value.translate(None, "'")

    except ConfigParser.NoOptionError as e:
        value = None

    return value


def get_yaml_config_value(configuration_file, option, verbose=False):
    import yaml

    stream = file(configuration_file, 'r')
    config = yaml.load(stream)
    value  = None

    try:
        # totally hacky way of doing this... can be improved
        if 3 == len(option.split('.')):
            # if config option depth is 3
            value = config[option.split('.')[0]][option.split('.')[1]][option.split('.')[2]]
        else:
            # else assume config option depth of 2
            value = config[option.split('.')[0]][option.split('.')[1]]

    except KeyError as e:
        value = None

    return value
