from smtplib import SMTP_SSL

from cornice import Service
from cornice.validators import colander_body_validator

from edwiges import logger
from edwiges.schema import EmailSchema
from edwiges.util import build_message

meta_service = Service(name='server_info', path='/')
mail_service = Service(name='mail', path='/mail')


@meta_service.get()
def status(request):

    logger.info("Status request received")

    settings = request.registry.settings
    host = settings['edwiges.provider_host']
    port = settings['edwiges.provider_port']

    with SMTP_SSL(host, port) as smtp:
        try:
            _, status = smtp.noop()
            errors = []

        except Exception as e:
            status = 'failed'
            errors = [str(e)]

    return {'status': status, 'errors': errors}


@mail_service.post(schema=EmailSchema(), validators=(colander_body_validator,))
def send_mail(request):

    settings = request.registry.settings

    logger.info("Send email request received",
                extra={'request': request.validated})

    host = settings['edwiges.provider_host']
    port = settings['edwiges.provider_port']
    username = settings['edwiges.provider_username']
    password = settings['edwiges.provider_password']

    with SMTP_SSL(host, port) as smtp:
        try:
            if username and password:
                smtp.login(username, password)

            smtp.send_message(
                msg=build_message(request.validated),
                from_addr=request.validated['sender'],
                to_addrs=request.validated['recipients'],
            )
            request.validated['status'] = 'sent'

            logger.info("Email sent",
                        extra={'request': request.validated})

        except Exception as e:
            request.validated['status'] = 'failed'
            request.validated['errors'] = [str(e)]

            logger.info("Send email request failed",
                        extra={'request': request.validated})
 
            # Precondition Failed
            request.response.status_code = 412

    return request.validated
