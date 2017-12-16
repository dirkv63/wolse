import platform
from competition import create_app
from waitress import serve


# Run Application
if __name__ == "__main__":
    if platform.node() == "CAA2GKCOR1":
        app = create_app('development')
    else:
        app = create_app('production')

    """
    with app.app_context():
        mg.User().register('dirk', 'olse')
    """

    if platform.node() == "CAA2GKCOR1":
        app.run()
    else:
        serve(app, listen='127.0.0.1:17103')
