import functions_framework
from json import dumps

@functions_framework.http
def test(request):
    args = dumps(dict(request.args))
    host = request.remote_addr
    json = request.get_json(silent=True)
    
    results = f"args = {args}\nhost = {host}\njson = {json}\n"

    return results
