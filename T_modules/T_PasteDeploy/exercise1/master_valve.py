if __name__ == '__main__':
    from paste import httpserver
    from paste.deploy import loadapp

    httpserver.serve(loadapp('config:configured.ini', relative_to='.'),
                     host='0.0.0.0', port='8080')
