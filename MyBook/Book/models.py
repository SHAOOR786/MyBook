from django.db import models

class Profile(models.Model):
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    PhoneNumber = models.CharField(max_length=12)
    Date_Of_Birth = models.DateField('Date of Birth')
    Password = models.CharField(max_length=300)

    def __str__(self):
        return self.Email


class Document(models.Model):
    Cv_Person = models.ForeignKey(Profile, on_delete=models.CASCADE)
    Cv = models.CharField(max_length=24)

    def __str__(self):
        return self.Cv

class Skill(models.Model):
    Skill_Person = models.ForeignKey(Profile, on_delete=models.CASCADE)
    Skill_Type = models.CharField(max_length=24)

    def __str__(self):
        return self.Skill_Type






# class Post(models.Model):
#     Post_Person= models.ForeignKey(Profile, on_delete=models.CASCADE)
#     Title = models.CharField(max_length=50)
#     Message = models.CharField(max_length=300)
#     like = models.IntegerField(default=0)

#     def __str__(self):
#         return self.Title

    

    