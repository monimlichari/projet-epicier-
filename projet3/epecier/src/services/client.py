from django.shortcuts import render
from django.shortcuts import render, redirect  
from src.forms.clientForm import ClientForm
from src.models import Client
from src.models import Credit
# Create your views here.

def clients(request): 
    admin=request.session['user_id']
    if request.method == "POST":  
        form = ClientForm(request.POST)  
        formcopy = ClientForm(request.POST.copy())
        formcopy.data['admin']=admin
        formcopy.data['total']=0
        if formcopy.is_valid():  
            try:  
                formcopy.save()  
                return redirect('/affiche/clients')  
            except:  
                pass 
        else:
            print(formcopy.errors) 
    else:  
        form = ClientForm()  
   
    return render(request,'client/ajoute_client.html',{'form':form,"pageClient":"active"})  
def show(request):
    admin=request.session['user_id']
    clients = Client.objects.filter(admin_id=admin) 
    return render(request,"client/affiche_client.html",{'clients':clients,"pageClient":"active","showClient":"active"})  
def search(request): 
    admin=request.session['user_id'] 
    print("admin id "+str(admin))   
    name=request.GET.get('name')
    clients = Client.objects.filter(nom__contains=name,admin_id=admin) 
    return render(request,"client/affiche_client.html",{'clients':clients,"pageClient":"active","showClient":"active","search":name})  

def edit(request, id):
    client = Client.objects.get(id=id)  
    return render(request,'client/edit_client.html', {'client':client,"pageClient":"active"})  
def update(request, id):  
    client = Client.objects.get(id=id)  
    admin=request.session['user_id']  
    formcopy = ClientForm(request.POST.copy(),instance = client)
    formcopy.data['admin']=admin
    formcopy.data['total']=client.total
    if formcopy.is_valid():  
        formcopy.save()  
        return redirect("/affiche/clients")  
    return render(request, 'client/edit_client.html', {'client': client,"pageClient":"active"})  
def destroy(request, id):  

    client = Client.objects.get(id=id)  
    client.delete()  
    return redirect("/affiche/clients")
def paye(request,id):
     client = Client.objects.get(id=id)  
     client.total=0
     client.save()
     Credit.objects.filter(client =id).update(etat = True)
     return redirect('/affiche/clients/')

