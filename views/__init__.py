from .app import app

# Carrega todas as rotas do blueprint
def all_routes(app):
    from .admin import administrator
    from .login import log_in
    from .index import ind
    from .profiles import profiles
    
    app.register_blueprint(administrator)
    app.register_blueprint(log_in)
    app.register_blueprint(ind)
    app.register_blueprint(profiles)
     

all_routes(app)

