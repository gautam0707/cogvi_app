import falcon
import mimetypes
import io

class StaticResource(object):
    def on_get(self, req, resp, filename):
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/html'
        if filename is "":
            filename = "index.html"
        else:
            filename = filename+'.html'
        with open('cogvi_web/'+filename, 'r') as f:
            resp.body = f.read()

class StaticAgiResource(object):
    def on_get(self, req, resp, filename):
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/html'
        filename = filename+'.html'
        with open('cogvi_web/agi/'+filename, 'r') as f:
            resp.body = f.read()


class ServeImages(object):
    def __init__(self, image_store):
        self._image_store = image_store

    def on_get(self, req, resp, name):
        resp.content_type = mimetypes.guess_type(name)[0]
        resp.stream = io.open(self._image_store+'/'+name, 'rb')


class ServeDocuments(object):
    def __init__(self):
        pass

    def on_get(self, req, resp, filename):
        resp.status = falcon.HTTP_200
        resp.content_type = 'application/pdf'
        with open('docs/'+filename, 'rb') as f:
            resp.body = f.read()


app = falcon.API()
app.add_route('/{filename}', StaticResource())
app.add_route('/agi/{filename}', StaticAgiResource())
app.add_route('/images/{name}', ServeImages('images'))
app.add_route('/docs/{filename}', ServeDocuments())