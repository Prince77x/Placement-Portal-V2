
from datetime import timedelta

class config:
     
    SECRET_KEY = "Backend",

    JWT_SECRET_KEY = 'Frontend',

    JWT_ACCESS_TOCKEN_EXPIRES = timedelta(hours=2)
