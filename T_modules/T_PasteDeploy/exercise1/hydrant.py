__author__ = 'Tony'


class Hydrant(object):
    def __init__(self, in_arg):
        self.in_arg = in_arg

    def __call__(self, environ, start_response):
        print 'Hydrant'
        status = '200 Ok'
        response_headers = [('Content-Type', 'text/plain')]
        start_response(status, response_headers)
        return ['%s, %s!\n' % (self.in_arg, 'Hydrant')]

def app_factory(global_config, in_arg):
    return Hydrant(in_arg)