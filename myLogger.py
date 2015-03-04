import MySQLdb
import datetime
from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('mySqlSettings.ini')
_serverName = parser.get('mysql_config', 'serverName')
_userName =  parser.get('mysql_config', 'userName') 
_password = parser.get('mysql_config', 'password')
_databaseName = parser.get('mysql_config', 'databaseName')

class myLogger():
    """Logs transactions for my devices."""

    def __Log(self, type=None, message=None,  deviceId=None, userName=None):
         
         try:
            db = MySQLdb.connect(_serverName, _userName, _password, _databaseName)
            curs= db.cursor()
            try:
                insert_stmt = ('INSERT INTO mylogs (log_type, log_message, device_id, log_date, username) '
                           'VALUES (%s, %s, %s, %s, %s)')
                data = (type, message, deviceId, datetime.datetime.now(), userName)
                curs.execute (insert_stmt, data)
                db.commit()
                print 'Data committed'
            except:
                print 'Error: the database is being rolled back'
                db.rollback()
            finally:
                db.close()
                print 'Connection closed!'
         except mysql.connector.Error as err:
            print 'Something went wrong: {}'.format(err)
         return

    def LogError(self, message=None, deviceId=None, userName=None):
        self.__Log('E', message, deviceId, userName)

    def LogInfo(self, message=None, deviceId=None, userName=None):
         self.__Log('I', message, deviceId, userName)

    def LogWarning(self, message=None, deviceId=None, userName=None):
         self.__Log('W', message, deviceId, userName)

    def LogDebug(self, message=None, deviceId=None, userName=None):
         self.__Log('D', message, deviceId, userName)

    def GetLog(self, type ):
        try:
            db = MySQLdb.connect(_serverName, _userName, _password, _databaseName,)
            curs= db.cursor(db.cursors.DictCursor)
            try:
                insert_stmt = ('INSERT INTO mylogs (log_type, log_message, device_id, log_date, username) '
                           'VALUES (%s, %s, %s, %s, %s)')
                data = (type, message, deviceId, datetime.datetime.now(), userName)
                
                curs.execute (insert_stmt, data)
                db.commit()
                print 'Data committed'
            except:
                print 'Error: the database is being rolled back'
                db.rollback()
            finally:
                db.close()
                print 'Connection closed!'
        except mysql.connector.Error as err:
           print 'Something went wrong: {}'.format(err)
        return

    def GetAllLogs(self):
        return



