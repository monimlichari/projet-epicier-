from django.db import models

# Create your models here.
class Admin(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    password =models.CharField(max_length=50)
    username = models.CharField(max_length=20)
    created_on = models.DateTimeField(auto_now_add=True)

class Client(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    addresse = models.CharField(max_length=255)
    phoneNumber = models.CharField(max_length=20)
    admin=models.ForeignKey(Admin, on_delete=models.CASCADE)
    total=models.FloatField()
    created_on = models.DateTimeField(auto_now_add=True)

# Create your models here.
class Produit(models.Model):
    nom = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images') 
    commentaire = models.TextField()
    prix=models.FloatField()
    admin=models.ForeignKey(Admin, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    
class Credit(models.Model):
    produit=models.ForeignKey(Produit, on_delete=models.CASCADE)
    client=models.ForeignKey(Client, on_delete=models.CASCADE)
    quantite=models.IntegerField()
    price=models.FloatField()
    total=models.FloatField()
    admin=models.ForeignKey(Admin, on_delete=models.CASCADE)
    etat=models.BooleanField(default=False)

   