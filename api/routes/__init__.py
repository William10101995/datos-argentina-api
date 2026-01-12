from .combustibles import combustibles_bp
from .icl import icl_bp
from .ipc import ipc_bp


def register_routes(app):
    app.register_blueprint(combustibles_bp)
    app.register_blueprint(icl_bp)
    app.register_blueprint(ipc_bp)
