from django.db.models import Model, CharField, IntegerField, TextField


class ContactClients(Model):
    names = CharField(max_length=200)
    age = IntegerField()
    address = CharField(max_length=200)
    email = CharField(max_length=50)
    company_name = CharField(max_length=50)
    city = CharField(max_length=50)
    phone = CharField(max_length=20)
    message = TextField()

    def __str__(self):
        return self.names
