from flask import Flask

def create_app():
    app = Flask(__name__)
    #encrypt and secure cookies and session data
    app.config['SECRET_KEY'] = 'chama'
    
    from .routes import approutes
    #from blueprints.auth.routes import auth_routes
    
    app.register_blueprint(approutes, url_prefix='/')
    #app.register_blueprint(auth_routes, url_prefix='/')
    
    return app