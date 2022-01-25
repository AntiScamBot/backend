from flask import Flask
import requests

app = Flask(__name__)

@app.route("/api/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/api/check/<domain>', timeout=10.0)
def check(domain):
    r = requests.get(url=f'https://{domain}')
    status_code = r.status_code 
    if status_code == 200:
        return status_code
    elif status_code != 200:
        return status_code
    
    
    
if __name__ == '__main__':
    app.run(debug=True)
