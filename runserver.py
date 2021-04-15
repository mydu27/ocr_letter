from app import create_app

app = create_app()


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    from werkzeug.serving import run_simple

    run_simple(hostname="0.0.0.0",
               port=8000,
               application=app,
               use_reloader=True,
               use_debugger=True,
               use_evalex=True,
               threaded=True)
