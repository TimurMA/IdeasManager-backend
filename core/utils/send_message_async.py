from django.core.mail import EmailMessage

from threading import Thread

class EmailThread(Thread):
    def __init__(self, subject, message, from_email, recipient_user):
        super(EmailThread, self).__init__()
        self.subject = subject
        self.message = message
        self.from_email = from_email
        self.recipient_user = recipient_user

    def run(self) -> None:
        msg = EmailMessage(self.subject, self.message, self.from_email, [self.recipient_user])
        msg.send()