from flask import Flask, jsonify
import requests

"""__all__ = (
    'check',
)"""

app = Flask(__name__)

@app.route("/api/")
def api():
    return "<p>API for the AntiScam Bot.</p>"


@app.route('/api/check/<domain>', methods=["GET"])
def check(domain):
    r = requests.get(url=f'https://{domain}').status_code
    if r:
        return jsonify(code=r)

    
if __name__ == '__main__':
    app.run(debug=False)