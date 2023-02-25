from django.shortcuts import redirect, render
from src.forms.adminForm import AdminForm
from src.models import Admin

def register(request):
    print("enter register ")
    if request.method == "POST":  
        form = AdminForm(request.POST) 
        if form.is_valid():    
            try:  
                form.save()  
                return redirect('/admin/login')  
            except:  
                pass   
    
    return render(request,'admin/register.html',)

                  
    
def login(request):
     if request.method == "POST": 
      form = AdminForm(request.POST)  
      username=form.data['username']
      password=form.data['password']
      admin=Admin.objects.filter(username=username)
      if len(admin)==0:
          return render(request,"admin/login.html",{"err":"username incorrect !!"})
      if admin[0].password==password:
          request.session['user_id']=admin[0].id
          request.session['user_nom']=admin[0].nom
          request.session['user_prenom']=admin[0].prenom
          request.session['username']=admin[0].username
          return redirect('/affiche/credits/')
      else:
          return render(request,"admin/login.html",{"err":"password incorrect !!"})
        
     else:
         return render(request,"admin/login.html")
def logout(request):
    request.session['user_id']=None
    request.session['user_nom']=None
    request.session['user_prenom']=None
    request.session['username']=None
    return redirect('/admin/login')
         
    