from django.db import models

class Advisors(models.Model):
    name = models.CharField(max_length=10)
    profilepic = models.ImageField(name = None, width_field=None, height_field=None)
    advisor_id = models.IntegerField()

    def __str__(self):
        return self.name, self.profilepic, self.advisor_id


# Create your models here.
