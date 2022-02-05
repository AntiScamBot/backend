from flask import Flask, jsonify
import requests


app = Flask(__name__)

@app.route("/api/")
def hello_world():
    return "<p>API for the AntiScam Bot.</p>"


@app.route('/api/check/<domain>')
def check(domain):
    r = requests.get(url=f'https://{domain}')
    status_code = r.status_code 
    if status_code:
        return jsonify(code={status_code})

    
if __name__ == '__main__':
    app.run(debug=False)
