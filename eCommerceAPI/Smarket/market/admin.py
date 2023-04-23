# Register your models here.
from django.contrib import admin
from .models import *
# Register your models here.

class CustomUser(admin.ModelAdmin):
   fieldsets = (
      ["User Information", {"fields": ["fname","lname","age","city"]}],
      # ["Scholarship Information", {"fields": ["UsersCategory", "UsersProduct"]}]
       )
   list_display=("fname","lname","age","city","adult")
   search_fields=["fname","city"]
          # lma kan () fl search wl list fl list esht8l fl search drb error 
   
   
   
   # def Users(self, obj):
   #     return obj.Users.fname

         # to make the UsersProduct and UsersCategory in the admin page
         # using inline to make the User could be inherted in the Category and Product panel 
         #lma agy a3ml add for the Category a2dr a3ml add for the Users too

class inlineUser(admin.StackedInline):
   model = User
   extra = 3    
# class CustomCategory(admin.ModelAdmin):
#    fieldsets = (["Category Information",{"fields": ["CategoryName","description"]}])
# #    inlines=[inlineUser]
   
   
   
   #How lw 3aiza a2semha fieldsets m3 l inline
            #  ["User Information", {"fields": (" inlines=[inlineUser]",)}])
   # def UsersCategory(self, obj):
   #     return obj.UsersCategory.name
    
class inlineCategory(admin.StackedInline):
   model = Category
   extra = 1

class CustomProduct(admin.ModelAdmin):
   # inline=[inlineCategory]
   
   def UsersProduct(self, obj):
      return obj.UsersProduct.title
   
admin.site.register(User, CustomUser)
# admin.site.register(Category, CustomCategory)
admin.site.register(Product, CustomProduct)
 