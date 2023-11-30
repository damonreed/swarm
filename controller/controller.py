###
### swarm_mon - controller.py - app to coordinate cloud run instances
###

from google.auth import compute_engine
from google.auth.transport.requests import AuthorizedSession

credentials = compute_engine.Credentials()

authed_session = AuthorizedSession(credentials)

response = authed_session.get('https://test-container-tnhs7yvhla-uc.a.run.app')

print(response.text)