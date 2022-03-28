from django.contrib import admin
from users.models import Users, Verifier

# Register your models here.
admin.site.register(Users)
admin.site.register(Verifier)