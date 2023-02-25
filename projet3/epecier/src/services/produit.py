from django.shortcuts import render, redirect  
from src.forms.produitForm import ProduitForm
from src.models import Produit


def produits(request):  
    admin=request.session['user_id']
    if request.method == "POST":  
        
        formcopy = ProduitForm(request.POST.copy(),request.FILES)
        formcopy.data['admin']=admin
        if formcopy.is_valid():  
            try:  
                formcopy.save()  
                return redirect('/affiche/produit/')  
            except:  
                pass 
        else:
            print(formcopy.errors) 
    else: 
        form = ProduitForm()  
    return render(request,'produit/ajoute_produit.html',{'form':form,"pageProduct":"active"})  
def show(request): 
    admin=request.session['user_id'] 
    produits = Produit.objects.filter(admin_id=admin)  
    return render(request,"produit/affiche_produit.html",{'produits':produits,"pageProduct":"active","showProduct":"active"})  

def search(request):
    admin=request.session['user_id']
    name=request.GET.get('name')
    produits = Produit.objects.filter(nom__contains=name,admin_id=admin)
    return render(request,"produit/affiche_produit.html",{'produits':produits,"pageProduct":"active","showProduct":"active","search":name})  
def edit(request, id):  
    admin=request.session['user_id']
    produit = Produit.objects.get(id=id,admin_id=admin)  
    return render(request,'produit/edit_produit.html', {'produit':produit,"pageProduct":"active"})  
def update(request, id):  
    admin=request.session['user_id']
    product = Produit.objects.get(id=id,admin_id=admin)  
    form = ProduitForm(request.POST.copy(),request.FILES, instance = product)  
    form.data['admin']=admin
    if form.is_valid():  
        form.save()  
        return redirect("/affiche/produit/")  
    return render(request, 'produit/edit_produit.html', {'product': product,"pageProduct":"active"})  
def destroy(request, id):  
    product = Produit.objects.get(id=id)  
    product.delete()  
    return redirect("/affiche/produit/")