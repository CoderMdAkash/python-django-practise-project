from django.contrib import admin

from .models import Member
from .models import Student
from .models import Product

admin.site.register(Member)
admin.site.register(Student)
admin.site.register(Product)