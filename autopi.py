import web
import json
     
urls = (
      '/', 'index',
      '/autoStats', 'autoStats',
  )
app = web.application(urls, globals())

class index:

    def GET(self):
        form = web.input()
        web.header('Content-Type', 'application/json')
        #try:
        pyDict = {'userId':form.user_id,'userName':form.userName}
        #except:
        #    pyDict= {'Exception':'Attribute Execption'}
        print(Animals.DOG)
        return json.dumps(pyDict)
  
class autoStats:

    def GET(self):
        Types = Enum(["Lights1", "Lights2", "Lights3"])
        form = web.input()
        web.header('Content-Type', 'application/json')
        type = form.type
        action = form.action
        #todo Add logic to push to a Gpio pin.
        #try:
        pyDict = {'type':form.type,'action':form.action}
        #except:
        #    pyDict= {'Exception':'Attribute Execption'}
        return json.dumps(pyDict)
  
class Enum(set):
    def __getattr__(self, name):
        if name in self:
            return name
        raise AttributeError

if __name__ == "__main__":
      app.run()