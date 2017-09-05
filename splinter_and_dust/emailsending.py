# # using SendGrid's Python Library
# # https://github.com/sendgrid/sendgrid-python
# import sendgrid
# import os
# from sendgrid.helpers.mail import *

# # sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
# sg = sendgrid.SendGridAPIClient(apikey="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")
# from_email = Email("test@example.com")
# to_email = Email("jamessandersoon@gmail.com")
# subject = "Sending with SendGrid is Fun"
# content = Content("text/plain", "and easy to do anywhere, even with Python")
# mail = Mail(from_email, subject, to_email, content)


# response = sg.client.mail.send.post(request_body=mail.get())
# print(response.status_code)
# print(response.body)
# print(response.headers)

