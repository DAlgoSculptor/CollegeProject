from django.db import  models


# create your model here


class Danish (models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    address=models.TextField(max_length=300)





class Meta:

    db_table="DanishInformation"