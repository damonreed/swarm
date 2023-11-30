###
### swarm_mon - controller.py - app to coordinate cloud run instances
###

import google.auth

credentials, project = google.auth.default()

authed_session = google.auth.transport.requests.AuthorizedSession(credentials)

response = authed_session.get('https://test-container-tnhs7yvhla-uc.a.run.app')

print(response.text)