from email.encoders import encode_base64
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText


def build_message(payload):

    # mimey stuff
    msg = MIMEMultipart()
    msg.preamble = 'This is a multi-part message in MIME format.\n'
    msg.epilogue = ''

    body = MIMEMultipart('alternative')
    body.attach(MIMEText(payload['body'], 'html'))
    msg.attach(body)

    for attach in payload.get('attachments', []):
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attach['content'])
        encode_base64(part)
        part.add_header('Content-Disposition',
                        'attachment; filename="{}"'.format(attach['filename']))
        msg.attach(part)
    
    msg.add_header('From', payload['sender'])
    msg.add_header('To', ', '.join(payload['recipients']))
    msg.add_header('Subject', payload['subject'])

    if 'reply_to' in payload:
        msg.add_header('Reply-To', payload['reply_to'])

    return msg
