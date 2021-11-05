from django.db import models
from acc.models import User
# Create your models here.
class Board(models.Model):
    subject = models.CharField(max_length=100)
    writer = models.CharField(max_length=50)
    content = models.TextField()
    pubdate = models.DateTimeField()
    up = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.subject
    
    def summary(self):
        if len(self.content) > 20:
            return self.content[:20] + " .."
        return self.content

from acc.models import User

class Reply(models.Model):
    sub = models.ForeignKey(Board, on_delete=models.CASCADE)
    replyer = models.CharField(max_length=50)
    comment = models.TextField()

    def __str__(self):
        return self.replyer
    
    def rep_pic(self):
        u = User.objects.get(username=self.replyer)
        return u.getpic()

   