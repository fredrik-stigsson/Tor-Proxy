![Tor Proxy](/logo.png)

# Tor Proxy

![License: MIT](https://img.shields.io/badge/license-MIT-green.svg) [![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/fredrik-stigsson/Tor-Proxy/issues) ![Version 1.0.0](https://img.shields.io/badge/version-1.0.0-blue)

A proxy server that can get content from a Tor hidden service and return it to a web server like nginx or apache. Add the Onion hostaddress as a Host header and make a request to 127.0.0.1:5000 or 127.0.0.1:5000/some-page.

## Example
```bash
curl -H "Host: iubh5w4hz5izygmj6pryvv57xf66josb7m6kjow5jphavuodxyzzp7yd.onion" http://127.0.0.1:5000
```

---

## Installation
```bash
cd /opt (if you want the service to work out of the box)
git clone https://github.com/fredrik-stigsson/Tor-Proxy.git
cd Tor-Proxy
python3 -m venv .venv
. .venv/bin/activate (Linux)
.venv/Scripts/activate (Windows)
pip install -r requirements.txt
deactivate
```

---

## Enable Tor Proxy Service on production server
```bash
cp /opt/Tor-Proxy/tor-proxy.service /etc/systemd/system/tor-proxy.service
systemctl daemon-reload
systemctl enable tor-proxy
systemctl start tor-proxy
```