from django.contrib import admin
from .models import *
# Register your models here.
class MemberAdmin(admin.ModelAdmin):
  list_display = ("link", "expiration_date", "employee_name",)
admin.site.register(Linke,MemberAdmin)
admin.site.register(Add_video)
