from flask import Flask, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to the OAuth 2.0 Application!'

@app.route('/callback')
def callback():
    # Retrieve the authorization code from the callback query parameters
    code = request.args.get('code')
    if not code:
        return 'No authorization code provided', 400
    
    # Normally here you would exchange the code for an access token
    # For simplicity, just display the code
    return f'Authorization code received: {code}'

if __name__ == '__main__':
    # Start the Flask application on localhost port 5000
    app.run(host='0.0.0.0', port=5000, debug=False)
