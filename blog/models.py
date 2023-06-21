from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    #foreignKey allows for a user to have many different post but not the other3 way around.
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        #this func tells django to use the URL name "post_detail and pass in the pk"
        return reverse("post_detail", kwargs={"pk": self.pk})