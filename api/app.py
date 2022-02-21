from flask import Flask, jsonify, logging
import urllib


app = Flask(__name__)

@app.route("/api/")
def api():
    return "<p>API for the AntiScam Bot.</p>"


@app.route('/api/check/<domain>', methods=["GET"])
def check(domain):
    app.logger.info('Fetching status code...')
    response = urllib.request.urlopen(f'https://{domain}')
    status_code = response.getcode()
    if status_code:
        app.logger.info('Succesfully fetched...')
        return jsonify(code=status_code)
   
@app.route('/api/phishing/<domain>')
def phishing(domain):
    return "<p>In process!</p>"


if __name__ == '__main__':
    app.run(debug=False)