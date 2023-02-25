from django.shortcuts import render, redirect
from src.models import Client  
from src.forms.creditForm import CreditForm
from src.models import Credit
from src.models import Produit

# Create your views here.
def credits(request): 
    admin=request.session['user_id'] 
    if request.method == "POST":  
        form = CreditForm(request.POST)  
        formcopy = CreditForm(request.POST.copy())
        produit=Produit.objects.get(id=formcopy.data["produit"])
        formcopy.data["price"]=produit.prix
        formcopy.data["total"]=formcopy.data["price"]*float(formcopy.data["quantite"])
        formcopy.data["admin"]=admin
        client = Client.objects.get(id=formcopy.data["client"])  
        client.total=client.total+formcopy.data["total"]
        
        if formcopy.is_valid():
            try:  
                formcopy.save()  
                client.save()
                return redirect('/affiche/credits/')  
            except Exception as e:  
                print(e)
        else:
            print(form.errors)      

    else:  
        form = CreditForm() 
    produits=Produit.objects.filter(admin_id=admin)
    clients=Client.objects.filter(admin_id=admin)
    return render(request,'credit/ajoute_credit.html',{'form':form,'produits':produits,'clients':clients,"pageCredit":"active"})  
def show(request):  

    admin=request.session['user_id'] 
    credits = Credit.objects.filter(admin_id=admin)  
    clients=Client.objects.filter(admin_id=admin) 
    return render(request,"credit/affiche_credit.html",{'credits':credits,"pageCredit":"active","showCredit":"active","clients":clients})  

def searchClient(request):  
    admin=request.session['user_id'] 
    clients=Client.objects.filter(admin_id=admin)
    name=request.GET.get('name')
    credits = Credit.objects.filter(admin_id=admin,client__nom__contains=name)
    return render(request,"credit/affiche_credit.html",{'credits':credits,"pageCredit":"active","showCredit":"active","clients":clients,"search":name})
def edit(request, id):  
    
    admin=request.session['user_id'] 
    produits=Produit.objects.filter(admin_id=admin)
    clients=Client.objects.filter(admin_id=admin) 
    credit = Credit.objects.get(id=id,)  
    return render(request,'credit/edit_credit.html', {'credit':credit,'produits':produits,'clients':clients,"pageCredit":"active"})  
def update(request, id):  
    if request.session['user_id']==None:
          return redirect('/admin/login')
    admin=request.session['user_id'] 
    credit = Credit.objects.get(id=id)   
    formcopy = CreditForm(request.POST.copy(),instance = credit)
    formcopy.data["price"]=Produit.objects.get(id=formcopy.data["produit"]).prix
    formcopy.data["total"]=formcopy.data["price"]*float(formcopy.data["quantite"])
    client = Client.objects.get(id=credit.client.id)
    client.total=credit.total+(formcopy.data["total"]-credit.total)
    formcopy.data["admin"]=admin
    if formcopy.is_valid():  
        client.save()
        formcopy.save()  
        return redirect("/affiche/credits/")  
    return render(request, 'credit/edit_credit.htmlt.html', {'credit': credit,"pageCredit":"active"})  
def destroy(request, id):  
    
    credit = Credit.objects.get(id=id)  
    credit.delete()  
    return redirect("/affiche/credits/")
def paye(request, id):  
    
    credit = Credit.objects.get(id=id)  
    client = Client.objects.get(id=credit.client.id)
    client.total=client.total-credit.total
    client.save()
    credit.etat=True
    credit.save()
    return redirect("/affiche/credits/")