from django.db import models

# Create your models here.


class Courses(models.Model):
    Image = models.URLField(null=True)
    Title = models.CharField(max_length=100 , null=True)
    Subtitle = models.CharField(max_length=150 , null=True)
    Description = models.TextField(null=True)
    Objective = models.TextField(null=True)# what you will learn from Udemy
    Requirements = models.TextField(null=True)
    No_Of_Days = models.IntegerField(null=True , blank=True)
    Udemy_Link = models.URLField(null=True)
  

    def __str__(self):
        return str(self.Title) +  ' - '  + str(self.No_Of_Days)
    
    class Meta:
        ordering = ['-id']


class ContactForm(models.Model):
    Name = models.CharField(max_length=50 , null=True)
    Message = models.TextField(null=True)
    Email = models.EmailField(null=True)