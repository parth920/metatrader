from django.db import models
from django.contrib.auth import get_user_model


UserModel = get_user_model()

class UserProfile(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    pin = models.CharField(max_length=4)

    def __str__(self):
        return self.user.username


    
class MasterLogin(models.Model):
    CHOICES = [
        ('Exness-MT5Real', 'Exness-MT5Real'),
        ('Exness-MT5Real2', 'Exness-MT5Real2'),
        ('Exness-MT5Real3', 'Exness-MT5Real3'),
        ('Exness-MT5Real4', 'Exness-MT5Real4'),
        ('Exness-MT5Real5', 'Exness-MT5Real5'),
        ('Exness-MT5Real6', 'Exness-MT5Real6'),
        ('Exness-MT5Real7', 'Exness-MT5Real7'),
        ('Exness-MT5Real8', 'Exness-MT5Real8'),
        ('Exness-MT5Real9', 'Exness-MT5Real9'),
        ('Exness-MT5Real10', 'Exness-MT5Real10'),
        ('Exness-MT5Real11', 'Exness-MT5Real11'),
        ('Exness-MT5Real12', 'Exness-MT5Real12'),
        ('Exness-MT5Real14', 'Exness-MT5Real14'),
        ('Exness-MT5Real15', 'Exness-MT5Real15'),
        ('Exness-MT5Real17', 'Exness-MT5Real17'),
        ('Exness-MT5Real18', 'Exness-MT5Real18'),
        ('Exness-MT5Real19', 'Exness-MT5Real19'),
        ('Exness-MT5Real20', 'Exness-MT5Real20'),
        ('Exness-MT5Real21', 'Exness-MT5Real21'),
        ('Exness-MT5Real22', 'Exness-MT5Real22'),
        ('Exness-MT5Real23', 'Exness-MT5Real23'),
        ('Exness-MT5Real24', 'Exness-MT5Real24'),
        ('Exness-MT5Trial', 'Exness-MT5Trial'),
        ('Exness-MT5Trial2', 'Exness-MT5Trial2'),
        ('Exness-MT5Trial3', 'Exness-MT5Trial3'),
        ('Exness-MT5Trial4', 'Exness-MT5Trial4'),
        ('Exness-MT5Trial5', 'Exness-MT5Trial5'),
        ('Exness-MT5Trial6', 'Exness-MT5Trial6'),
        ('Exness-MT5Trial7', 'Exness-MT5Trial7'),
        ('Exness-MT5Trial8', 'Exness-MT5Trial8'),
        ('Exness-MT5Trial9', 'Exness-MT5Trial9'),
        ('Exness-MT5Trial10', 'Exness-MT5Trial10'),
        ('Exness-MT5Trial11', 'Exness-MT5Trial11'),
        ('Exness-MT5Trial12', 'Exness-MT5Trial12'),
        ('Coinexx-Demo', 'Coinexx-Demo'),
    ]

    master_login = models.CharField(max_length=255)
    master_password = models.CharField(max_length=255)
    login = models.IntegerField()
    password = models.CharField(max_length=255)
    server = models.CharField(max_length=255,choices=CHOICES)
    
    

    def __str__(self):
        return f"MasterLogin {self.master_login}"

class Server(models.Model):
    server_name=models.CharField(max_length=255)
    server_id=models.CharField(max_length=255)
    

    def __str__(self):
        return f'adminlogin {self.server_name}'
    


