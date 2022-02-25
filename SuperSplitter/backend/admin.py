from django.contrib import admin
from .models import User, Session, Tag, Currency, Payment

# Register your models here.
admin.site.register(User)
admin.site.register(Session)
admin.site.register(Tag)
admin.site.register(Currency)
admin.site.register(Payment)

