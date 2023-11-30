###
### swarm_mon - controller.py - app to coordinate cloud run instances
###

import google.auth
from google.auth.transport.requests import AuthorizedSession

credentials, project = google.auth.default()

authed_session = AuthorizedSession(credentials)

response = authed_session.get('https://test-container-tnhs7yvhla-uc.a.run.app')

print(response.text)