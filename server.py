import falcon


class StaticResource(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/html'
        with open('cogvi_web/index.html', 'r') as f:
            resp.body = f.read()

app = falcon.API()
app.add_route('/', StaticResource())