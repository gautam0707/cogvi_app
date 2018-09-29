import falcon
import mimetypes
import io

class StaticResource(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/html'
        with open('cogvi_web/index.html', 'r') as f:
            resp.body = f.read()


class ServeImages(object):
    def __init__(self, image_store):
        self._image_store = image_store

    def on_get(self, req, resp, name):
        resp.content_type = mimetypes.guess_type(name)[0]
        resp.stream = io.open(self._image_store+'/'+name,'rb')

app = falcon.API()
app.add_route('/', StaticResource())
app.add_route('/images/{name}',ServeImages('images'))