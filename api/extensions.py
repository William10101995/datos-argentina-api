from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

cors = CORS()
limiter = Limiter(key_func=get_remote_address)
