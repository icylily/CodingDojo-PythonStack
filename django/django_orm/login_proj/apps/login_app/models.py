from django.db import models
import re
import bcrypt 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your models here.


class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData["first_name"]) < 2:
            errors["first_name"] = "Firstname should be at least 2 characters."
        if len(postData["last_name"]) < 2:
            errors["last_name"] = "Lastname should be at least 2 characters."
        if not EMAIL_REGEX.match(postData['email']):
            errors["email"] = "Please input a vilid email address."
        if len(postData["password"])<8:
            errors["password"]="Passworsd should be at least 8 characters"
        if postData["password"]!= postData["re_password"]:
            errors["password"]="Please re-enter the same password!"
        if len(self.filter(email=postData["email"])) > 0:
            errors["existed"] = "This  email already existed!"
            
        # release_date = datetime.strptime(postData["release_date"], '%Y-%m-%d')
        # recent_date = datetime.now()
        # if release_date > recent_date:
        #     errors["release_date"] = "Release date should be in the past"
        # if len(self.filter(title=postData["title"])) > 0:
        #     errors["existed"] = "This  title already existed!"
        return errors
    def login_validator(self,postData):
        errors={}
        if not EMAIL_REGEX.match(postData['email']):
            errors["email"] = "Please input a vilid email address."
        if len(self.filter(email=postData["email"]))<1:
            errors["email"] = "No such email ,please re-enter another one or go to registration!"
        if bcrypt.checkpw(postData["password"].encode(), self.filter(email=postData["email"])[0].password.encode()) != True:
            errors["password"] = "password encorrect"
        return errors
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    objects = ShowManager()


