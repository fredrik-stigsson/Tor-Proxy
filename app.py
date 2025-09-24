#!/usr/bin/env python3
from flask import Flask, request, Response
import socks, http.client, os

# Create the app
app = Flask(__name__)

# Default route
@app.route("/", defaults={"path": ""}, methods=["GET","POST","PUT","DELETE","PATCH","OPTIONS","HEAD"])
@app.route("/<path:path>", methods=["GET","POST","PUT","DELETE","PATCH","OPTIONS","HEAD"])
def index(path):

    # Get headers
    host = request.headers.get("Host", "")
    
    # Make sure that it is a onion address
    if not host.endswith(".onion"):
        return Response("Host must be a .onion address", status=400)

    # Connect via Tor SOCKS
    sock = socks.socksocket()
    sock.set_proxy(socks.SOCKS5, "127.0.0.1", 9050)
    sock.connect((host, 80))

    # Forward original request
    conn = http.client.HTTPConnection(host, 80)
    conn.sock = sock
    conn.request(
        method=request.method,
        url="/" + path,
        body=request.get_data(),
        headers={k: v for k, v in request.headers if k.lower() not in ("host", "connection")}
    )
    resp = conn.getresponse()
    data = resp.read()
    headers = {k: v for k, v in resp.getheaders() if k.lower() not in ("transfer-encoding", "connection")}
    conn.close()

    # Return response
    return Response(data, status=resp.status, headers=headers)