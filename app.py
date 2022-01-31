from flask import Flask
import requests


app = Flask(__name__)

@app.route("/api/")
def hello_world():
    return "<p>API for the AntiScam Bot.</p>"


@app.route('/api/check/<domain>', methods=["GET"])
def check(domain):
    # Ratelimit: 60 seconds per 1 request
    r = requests.get(url=f'https://{domain}')
    status_code = r.status_code 
    if status_code == 200:
        return status_code
    elif status_code != 200:
        return status_code
    
if __name__ == '__main__':
    app.run(debug=True)