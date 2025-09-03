from os import environ
import json

print(f"Environment Variables:\n{json.dumps(dict(environ), indent=4)}")
print(f"Log_LEVEL: {environ.get('LOG_LEVEL', 'Not Set')}")
print(f"EV length: {len(environ)}")