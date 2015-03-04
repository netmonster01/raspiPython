import MySQLdb
import datetime
from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('mySqlSettings.ini')
_serverName = parser.get('mysql_config', 'serverName')
_userName =  parser.get('mysql_config', 'userName') 
_password = parser.get('mysql_config', 'password')
_databaseName = parser.get('mysql_config', 'databaseName')


class myDevice(object):
    """description of class"""


    def deviceExists(self, device_id):
        return True

    def addDevice(self,deviceId= None,ipAddress= None, mac=None):
        return


