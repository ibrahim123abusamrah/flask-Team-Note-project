import os
from flask import Flask ,render_template
import requests
import json 

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    from . import db
    db.init_app(app)

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    from . import auth
    app.register_blueprint(auth.bp)
    
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    # a simple page that says hello
    @app.route('/hello')
    def hello( charset='utf-8'):
        requestUrl = "http://localhost:3000/customer/v1.0/API/TenantID"
        requestHeaders = {
            "apikey": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0ZW5hbnRJZCI6ImRjMDM3YzViLTM4ODYtNDA0ZS1hZmZiLTE5NjZhNDQ2ZTNjMSIsInNlY3JldEtleSI6Ii1AK3llYWolZmM0YWVhZCQwNygtd2hidGtocWMmd2M9cmNhbnd1M2RtM3EqeiElYTliIiwiaWF0IjoxNjAzMzA1ODc4fQ.yn1mz_qQGbkNsbL9LCHUtjOvWxshT5frtDx048B9H-Q",
            "Accept": "application/json"
        }
        param ={

        }
        request = requests.get(requestUrl, headers=requestHeaders)

        print request.content
        return render_template('done.html', movies=request.text)
    return app
    