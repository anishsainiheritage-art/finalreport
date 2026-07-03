from django.contrib import admin

# Register your models here.

from .models import Report
from .models import Buyer

admin.site.register(Buyer)



admin.site.register(Report)