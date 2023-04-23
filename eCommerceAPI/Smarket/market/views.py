from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from market.models import User,Order,Category,Product
# from market.forms import UserForm,TrackForm,CourseForm

def home(request):
     return HttpResponse ('<h1>Hello This is Home Page</h1> ')
   #  return render(request, 'market/home.html')

# http response ka2ny b3ml print 3l console lakn render ka2ny bktp f file bysm3 3shan a3ml render 3la html page
def getUser(request, u_id):
   u=User.objects.get(id=u_id)
   context={'user':u}
   return render(request,'market/user.html', context)
   # return HttpResponse ('<h1>Hello This is The User Page of User No.'  + st_id + '<h1> and his name is '+ st.fname + ' ' + st.lname)


def getUsers(request):
   allusers=User.objects.all()
   # esm l variable eli hyru7 ll template wl value asln bta3u eli gebtu fl variable eli fu2 
   context={'users':allusers}
   return render(request,'market/allusers.html', context)
   # return render(request, 'market/allusers.html', {'users':allusers})



def newUser(request):
   uForm=UserForm()   #this is an empty form the above is save the form 
   if request.method=='POST':
      uForm=UserForm(request.POST)
      if uForm.is_valid():
         uForm.save()
         # return HttpResponse('User Added Successfully')
         # it takes me the url and hit the function of it 
         return HttpResponseRedirect(redirect_to='/market/allusers/')
   context={'u_form' : uForm}
   return render(request,'market/newuser.html', context)



def editUser(request,u_id):
   u=User.objects.get(id=u_id)
   uForm=UserForm(instance=u)
   if request.method=='POST':
      uForm=UserForm(request.POST,instance=u)
      if uForm.is_valid():
         uForm.save()
         return HttpResponseRedirect(redirect_to='/market/allusers/')
   context={'u_form' : uForm}
   return render(request,'market/newuser.html', context)



def deleteUser(request,u_id):
   u=User.objects.get(id=u_id)
   # if request.method=='POST':
   u.delete()
   return HttpResponseRedirect(redirect_to='/market/allusers/') 