###
### swarm_mon - controller.py - app to coordinate cloud run instances
###

from google.oauth2 import id_token
from google.auth import compute_engine
# from google.oauth2 import service_account
import google.auth
import google.auth.transport.requests
from google.auth.transport.requests import AuthorizedSession

# target_audience = 'https://your-cloud-run-app.a.run.app'
url = 'https://test-container-tnhs7yvhla-uc.a.run.app'

#creds = service_account.IDTokenCredentials.from_service_account_file(
#        '/path/to/svc.json', target_audience=target_audience)
request = google.auth.transport.requests.Request()
creds = compute_engine.IDTokenCredentials(request,target_audience=url)

authed_session = AuthorizedSession(creds)

# make authenticated request and print the response, status_code
resp = authed_session.get(url)
print(resp.status_code)
print(resp.text)

# to verify an ID Token
request = google.auth.transport.requests.Request()
token = creds.token
print(token)
print(id_token.verify_token(token,request))

