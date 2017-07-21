import colander


class EmailSequenceSchema(colander.SequenceSchema):
    email = colander.SchemaNode(colander.String(), 
                                validator=colander.Email())


class EmailAttachmentSchema(colander.SequenceSchema):  

    @colander.instantiate()
    class Attachement(colander.MappingSchema):
        filename = colander.SchemaNode(colander.String())
        content = colander.SchemaNode(colander.String())


class EmailSchema(colander.MappingSchema):
    sender = colander.SchemaNode(colander.String(),
                                 validator=colander.Email())
    recipients = EmailSequenceSchema()
    cc = EmailSequenceSchema(missing=colander.drop)
    cco = EmailSequenceSchema(missing=colander.drop)
    subject = colander.SchemaNode(colander.String())
    body = colander.SchemaNode(colander.String())
    attachments = EmailAttachmentSchema(missing=colander.drop)
    reply_to = colander.SchemaNode(colander.String(),
                                   validator=colander.Email(),
                                   missing=colander.drop)
