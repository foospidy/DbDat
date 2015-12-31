import ConfigParser
import StringIO
import os

def get_pg_config_value(configuration_file, option, verbose=False):
	# postgresql config files do not have sections, so inject a dummy section
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
