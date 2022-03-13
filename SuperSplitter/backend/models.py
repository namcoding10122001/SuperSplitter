from django.db import models


class User(models.Model):
    name = models.CharField(max_length=200)
    dob = models.DateField()
    email = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True, unique=True, editable=False)

    def __str__(self):
        return self.name


class Session(models.Model):
    spender = models.ForeignKey(User, related_name='%(class)s_spender', on_delete=models.CASCADE)
    participants = models.ManyToManyField(User, blank=True)
    date_time = models.DateTimeField()
    place_name = models.TextField(max_length=1000, null=True, blank=True)
    total_spent = models.FloatField()
    tags = models.ManyToManyField('Tag', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True, unique=True, editable=False)

    def __str__(self):
        return " || ".join([self.place_name, self.date_time.strftime("%Y/%m/%d, %H:%M:%S"), str(self.spender), str(self.total_spent)])


class Tag(models.Model):
    tag_name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True, unique=True, editable=False)

    def __str__(self):
        return self.tag_name
