from flask import Flask, jsonify, request

app = Flask(__name__)

from sender import sendEmail
from access_control import crossdomain

@app.route('/send/london-consent-project', methods=['POST'])
@crossdomain(origin='*')
def index():
	print "Hit send email endpoint"
	sendEmail(request.form.getlist('name')[0], request.form.getlist('email')[0], request.form.getlist('subject')[0], request.form.getlist('message')[0]+'\n\nSent from London Consent Project contact form')
	return jsonify({'success': 'true'})

if __name__ == '__main__':
	app.run(debug=True)