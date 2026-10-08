from twisted.application import service, internet
from twisted.web import server, resource
class Greeting(resource.Resource):
    isLeaf = True
    def render_GET(self, request):
        return b"Hello, World!\n"
application = service.Application("CorpusGreeting")
internet.TCPServer(8080, server.Site(Greeting()), interface="127.0.0.1").setServiceParent(application)
