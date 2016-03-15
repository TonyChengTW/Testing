__author__ = 'Tony'

class DrinkingFountain(object):
    def __init__(self, in_arg):
        self.in_arg = in_arg

    def __call__(self, environ, start_response):
        print 'DrinkingFountain'
        status = '200 Ok'
        response_headers = [('Content-Type', 'text/plain')]
        start_response(status, response_headers)
        return ['%s, %s!\n' % (self.in_arg, 'DrinkingFountain')]
    def app_factory(global_config, in_arg):
        return DrinkingFountain(in_arg)