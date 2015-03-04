import cherrypy
import MySQLdb
import json
import myLogger

# Variables
_serverName = '192.168.0.114'
_userName = 'mypi'
_password = 'raspberry01'
_databaseName = 'myFirstPythonDB'


class MyFirstDB:

    def updateDB(self, firstName, lastName):
        try:
            db = MySQLdb.connect(_serverName, _userName, _password, _databaseName)
            curs= db.cursor()
            try:
                insert_stmt = ('INSERT INTO myFirstTable (firstName, lastName) '
                           'VALUES (%s, %s)')
                data = (firstName, lastName)
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

    def index(self, firstName, lastName):
        lname = cherrypy.request.params.get('lastName', None)
        fname = cherrypy.request.params.get('firstName', None)
        myLogger.myLogger.LogDebug(self,'Hello World!!!', 'D', 1 )
        #try to update the database
        self.updateDB(fname, lname)
        return lname + ', ' + fname
    index.exposed = True

#cherrypy.config.update({'server.socket_host': '0.0.0.0'})
cherrypy.quickstart(MyFirstDB())

if __name__ == '__main__':    
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    cherrypy.quickstart(MyFirstDB())


