from django.db import models

# Create your models here.
class login_table(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    type=models.CharField(max_length=100)

class user_table(models.Model):
    LOGIN=models.ForeignKey(login_table,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.BigIntegerField()
    place=models.CharField(max_length=100)
    # image=models.CharField(max_length=100)

class hospital_table(models.Model):
    LOGIN=models.ForeignKey(login_table,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.BigIntegerField()
    place=models.CharField(max_length=100)
    post=models.CharField(max_length=100)
    pin=models.IntegerField()
    district=models.CharField(max_length=100)

class vaccinedetails_table(models.Model):
    HOSPITAL=models.ForeignKey(hospital_table,on_delete=models.CASCADE)
    vaccinename=models.CharField(max_length=100)
    details=models.CharField(max_length=100)
    dateupto=models.DateField()
    uploadeddate=models.DateField()

class rating_table(models.Model):
    USER=models.ForeignKey(user_table,on_delete=models.CASCADE)
    rating=models.CharField(max_length=100)
    feedback=models.CharField(max_length=100)
    date=models.DateField()
    HOSPITAL=models.ForeignKey(hospital_table,on_delete=models.CASCADE)




class petshop_table(models.Model):
    LOGIN=models.ForeignKey(login_table,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    phone=models.BigIntegerField()
    email=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    pin=models.IntegerField()
    post=models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    license=models.CharField(max_length=100)



class services_table(models.Model):
    PETSHOP=models.ForeignKey(petshop_table,on_delete=models.CASCADE)
    servicename=models.CharField(max_length=100)
    details=models.CharField(max_length=100)

class request_table(models.Model):
    USER = models.ForeignKey(user_table, on_delete=models.CASCADE)
    SERVICES=models.ForeignKey(services_table,on_delete=models.CASCADE)
    request=models.CharField(max_length=100)
    date=models.DateField()
    status=models.CharField(max_length=100)

class petshoprequest_table(models.Model):
    USER = models.ForeignKey(user_table, on_delete=models.CASCADE)
    PETSHOP = models.ForeignKey(petshop_table, on_delete=models.CASCADE)
    pettype=models.CharField(max_length=100)
    age=models.CharField(max_length=100)
    date=models.DateField()
    details=models.CharField(max_length=100)
    status=models.CharField(max_length=100)

class pet_table(models.Model):
    SHOP = models.ForeignKey(petshop_table, on_delete=models.CASCADE)
    petname=models.CharField(max_length=100)
    image=models.CharField(max_length=100)
    type=models.CharField(max_length=100)
    age=models.CharField(max_length=100)
    price=models.IntegerField()

class complaints_table(models.Model):
    USER = models.ForeignKey(user_table, on_delete=models.CASCADE)
    complaints=models.CharField(max_length=100)
    reply=models.CharField(max_length=100)
    date=models.DateField()




class Chat(models.Model):
    FROMID= models.ForeignKey(login_table,on_delete=models.CASCADE,related_name="Fromid")
    TOID= models.ForeignKey(login_table,on_delete=models.CASCADE,related_name="Toid")
    message=models.CharField(max_length=100)
    date=models.DateField()


class vaccine_request_table(models.Model):
    USER = models.ForeignKey(user_table, on_delete=models.CASCADE)
    VACCINE = models.ForeignKey(vaccinedetails_table, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    request = models.CharField(max_length=100)
    date = models.DateField()


class tips_table(models.Model):
    HOSPITAL = models.ForeignKey(hospital_table, on_delete=models.CASCADE)
    tips = models.CharField(max_length=100)
    details = models.CharField(max_length=200)
    pet_type = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    date = models.DateField()



class post_table(models.Model):
    USER = models.ForeignKey(user_table, on_delete=models.CASCADE)
    file = models.CharField(max_length=500)
    details = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    date = models.DateField()



class comment_table(models.Model):
    POST = models.ForeignKey(post_table, on_delete=models.CASCADE)
    USER = models.ForeignKey(user_table, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)
    date = models.DateField()



class user_pet_table(models.Model):
    USER = models.ForeignKey(user_table, on_delete=models.CASCADE)
    petname=models.CharField(max_length=100)
    image=models.CharField(max_length=100)
    type=models.CharField(max_length=100)
    age=models.CharField(max_length=100)
    price=models.IntegerField()