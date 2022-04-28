from django.db import models

class Userlogins(models.Model):
    username = models.CharField(primary_key=True, max_length=30)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    phonenumber = models.CharField(max_length=20)
    
    def register(self):
        self.save()


    @staticmethod
    def get_username_by_email(email):
        try:
            return Userlogin.objects.get(email= email)
        except:
            return False


    def isExists(self):
        if Userlogin.objects.filter(email = self.email):
            return True

        return False
