from configparser import ConfigParser
import os
class Config(object):



	def __init__(self):

		self.production_server_enable = None
		self.production_server_hostname = None
		self.production_server_port = None
		self.production_server_username = None
		self.production_server_password  = None
		self.production_server_timeout = None

		self.production_database_enable = None
		self.productin_database_hostname = None
		self.production_database_port = None
		self.production_database_username = None
		self.production_database_password  = None
		self.production_database_timeout = None

		self.sandbox_server_enable = None
		self.sandbox_server_hostname = None
		self.sandbox_server_port = None
		self.sandbox_server_username = None
		self.sandbox_server_password  = None
		self.sandbox_server_timeout = None

		self.log_enable = None
		self.log_name = None
		self.log_size_limit = None
		self.log_file_limit = None


	# convert human sizes to bytes
	def convert_bytes(self,byts):
	    try:
	        byts = byts.lower()
	        if byts.endswith('kb'):
	            return int(byts[0:-2]) * 1024
	        elif byts.endswith('mb'):
	            return int(byts[0:-2]) * 1024 * 1024
	        elif byts.endswith('gb'):
	            return int(byts[0:-2]) * 1024 * 1024 * 1024
	        
	        # for anything else... just throw an exception, we care zero
	        raise IOError('Invalid input. Correct format: #kb/#mb/#gb like 10gb or 5mb')
	        
	    except Exception as error:
	        raise Exception('Invalid input. Correct format: #kb/#mb/#gb like 10gb or 5mb. An error ' +
	                        repr(error) + ' occurred.')



	def configure(self):
		#ensure that the config file exist
		curr_dir = os.path.dirname(os.path.abspath(__file__))
		config_file = curr_dir+"/config.ini"

		#ensure config file not missing
		if not os.path.isfile(config_file):
			raise Exception("Config.ini file missing!")

		
		#all is cood so we will continue parsing
		config = ConfigParser()
		if not config.read(config_file):
			raise IOError("Could not read the config file ",config_file)

		#ections = config.sections()

		#configure the production
		self.configure_production_server(config)

		self.configure_production_database(config)

		self.configure_sandbox_server(config)


	def configure_production_server(self,config):

		try:
			server = config['Production_server']
		except:
			raise KeyError("[Production_server] and its related data might be missing from config.ini")
		
		self.production_server_enable = self.__toBoolean(server.get('enable'))
		self.production_server_hostname = server.get('hostname');
		self.production_server_port = server.get('port')
		self.production_server_username = server.get('username')
		self.production_server_password = server.get('password')
		self.production_server_timeout = server.get('timeout')

		self.__checkProductionSetup()



	def configure_production_database(self,config):

		try:
			server = config['Production_database_server']
		except:
			raise KeyError("[Production_database_server] and its related data might be missing from config.ini")

		self.production_database_enable = self.__toBoolean(server.get('enable'))
		self.production_database_server_hostname = server.get('hostname');
		self.production_database_server_port = server.get('port')
		self.production_database_server_username = server.get('username')
		self.production_database_server_password = server.get('password')
		self.production_database_server_timeout = server.get('timeout')


	def configure_sandbox_server(self,config):

		try:
			server = config['Sandbox_server']
		except:
			raise KeyError("[Sandbox_server] and its related data might be missing from config.ini")
		
		self.sandbox_server_enable = self.__toBoolean(server.get('enable'))
		self.sandbox_server_hostname = server.get('hostname');
		self.sandbox_server_port = server.get('port')
		self.sandbox_server_username = server.get('username')
		self.sandbox_server_password = server.get('password')
		self.sandbox_server_timeout = server.get('timeout')



	def __toBoolean(self,string):
		
		string = string.lower()
		


	def __checkProductionSetup(self):
		if self.production_server_enable == True:
			print("Checking production server configuration....")
			print("------------------------------------------")
			if self.production_server_hostname:
				print("production server hostname OK")
			else:
				print("production server hostname invalid")
			if self.production_server_port:
				try:
					self.production_server_port = int(self.production_server_port)
					print("production server port ok")
				except:
					print("Production server port invalid")












