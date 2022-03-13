from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User as DjangoUser


class User(models.Model):
    user = models.OneToOneField(DjangoUser, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200)
    dob = models.DateField(null=True, blank=True)
    email = models.EmailField()
    avatar = models.ImageField(null=True, blank=True, upload_to='storage')
    created = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True, unique=True, editable=False)

    def __str__(self):
        return str(self.user)


class Session(models.Model):
    title = models.CharField(max_length=200, default="Session")
    creator = models.ForeignKey(User, related_name='%(class)s_creator', on_delete=models.SET_NULL, null=True)
    participants = models.ManyToManyField(User, blank=True)
    date_time = models.DateTimeField()
    place_name = models.TextField(max_length=1000, null=True, blank=True)
    total_spent = models.FloatField()
    currency = models.ForeignKey('Currency', editable=True, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField('Tag', blank=True)
    last_updated = models.DateTimeField(editable=True, default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True, unique=True, editable=False)
    finish = models.BooleanField(default=False, editable=True, null=False, blank=False)

    def __str__(self):
        return " | ".join([self.place_name, self.date_time.strftime("%Y/%m/%d, %H:%M:%S"), str(self.creator), str(self.total_spent)])


class Tag(models.Model):
    tag_name = models.CharField(max_length=200)
    default_tag = models.BooleanField(default=True, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    id = models.AutoField(primary_key=True, unique=True, editable=False)

    def __str__(self):
        return self.tag_name


class Payment(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    payer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    split_ratio = models.FloatField()
    currency = models.ForeignKey('Currency', editable=True, on_delete=models.SET_NULL, null=True)
    paid_amount = models.IntegerField(default=0, editable=True, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, editable=False, null=True, blank=True)
    last_updated = models.DateTimeField(editable=True, default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True, unique=True, editable=False)

    def __str__(self):
        return ' | '.join([self.session.title, self.date.strftime('%Y/%m/%d'), str(self.payer), str(self.paid_amount)])
        # return ' | '.join([self.session.title, self.date.strftime('%Y/%m/%d'), str(self.payer), str(self.paid_amount) + " " + (self.currency.abbreviation if self.currency && self.currency.abbreviation else "") ])


class Currency(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, editable=True)
    symbol = models.CharField(max_length=2, null=False, blank=False, editable=True)
    abbreviation = models.CharField(max_length=3, null=False, blank=False, editable=True)
    coefficient = models.FloatField(editable=True, null=False, blank=False)
    last_updated = models.DateTimeField(editable=True, default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True, unique=True, editable=False)

    def __str__(self):
        return ' | '.join([self.name, str(self.coefficient)])
