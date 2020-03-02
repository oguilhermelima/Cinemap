from .app import app

from controller.index import index
from controller.login import log_in
from controller.admin import administrator
from controller.profiles import profiles

app.register_blueprint(index)
app.register_blueprint(log_in)
app.register_blueprint(administrator)
app.register_blueprint(profiles)
