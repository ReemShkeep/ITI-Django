from django import forms
# from iot.models import * 
from iot.models import Student,Track,Course

class UserForm(forms.ModelForm):
    class Meta:
       model=User
       fields='__all__'
      #  fields=['fname','lname','age','studentsTrack']

class CategoryForm(forms.ModelForm):
   class Meta:
      model=Category
      fields=['name','description','courses']



class ProductForm(forms.ModelForm):
   class Meta:
      model=Product
   #  because it's tuble and if it takes one parameter 
      fields=('title',)      
      # fields=['title','description','hours']
      
   