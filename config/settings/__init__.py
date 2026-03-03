import os

_env = os.environ.get("DJANGO_ENV", "development")
if _env == "production":
    from .production import *
else:
    from .development import *
