from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserCreationForm,UserChangeForm
from .models import User

class UserAdmin(BaseUserAdmin):
  form = UserChangeForm
  add_form = UserCreationForm

  list_display = ('name', 'email', 'nick_name', 'phone_number', 'is_admin')
  list_filter = (
    (None,{'fields':('name','email','password')}),
    ("Personal info",{'fields':('address','phone_number')}),
    ("Permissions",{'fields':('is_admin',)})
  )
  add_fieldsets = (
    (None, {
      'classes':('wide',),
      'fields': ('name', 'email', 'nick_name', 'phone_number', 'password1', 'password2')
    }),
  )
  search_fields = ('email',)
  ordering = ('email',)
  filter_horizontal = ()

admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
