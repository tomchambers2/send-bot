import mandrill

def sendEmail(name, email, subject, message):
	try:
		print "Sending email to %s", email
		mandrill_client = mandrill.Mandrill('DuIMK8qbJHaZYYAvfET5gQ')
		message = {
		 'auto_html': None,
		 'auto_text': None,
		 'from_email': email,
		 'from_name': name,
		 'headers': {'Reply-To': email},
		 'metadata': {'website': 'www.example.com'},
		 'preserve_recipients': None,
		 'recipient_metadata': [{'rcpt': 'info@thelcp.com',
								 'values': {'user_id': 123456}}],
		 'return_path_domain': None,
		 'signing_domain': None,
		 'subject': subject,
		 'tags': ['password-resets'],
		 'text': message,
		 'to': [{'email': 'info@thelcp.com',
				 'name': 'London Consent Project',
				 'type': 'to'}],
		 'track_clicks': None,
		 'track_opens': None,
		 'tracking_domain': None,
		 'url_strip_qs': None,
		 'view_content_link': None}
		result = mandrill_client.messages.send(message=message, async=False, ip_pool='Main Pool')

	except mandrill.Error, e:
		# Mandrill errors are thrown as exceptions
		print 'A mandrill error occurred: %s - %s' % (e.__class__, e)
		# A mandrill error occurred: <class 'mandrill.UnknownSubaccountError'> - No subaccount exists with the id 'customer-123'    
		raise
