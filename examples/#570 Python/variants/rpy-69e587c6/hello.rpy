from twisted.web.resource import Resource
class Greeting(Resource):
    isLeaf = True
    def render_GET(self, request):
        request.setHeader(b"content-type", b"text/plain; charset=utf-8")
        return b"Hello, World!\n"
resource = Greeting()
