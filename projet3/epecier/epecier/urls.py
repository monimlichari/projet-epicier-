"""epecier URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

import src.services.admin as adminView
import src.services.client as clietView
import src.services.produit as produitView
import src.services.credit as creditView


urlpatterns = [
    path('admin/login/', adminView.login),  
    path('admin/logout/', adminView.logout),  
    path('admin/register/', adminView.register),  


    path('ajoute/client/', clietView.clients),  
    path('affiche/clients/', clietView.show),  
    path('edit/client/<int:id>', clietView.edit),  
    path('update/client/<int:id>', clietView.update),  
    path('delete/client/<int:id>', clietView.destroy),  
    path('clients/search', clietView.search),
    path('client/paye/<int:id>',clietView.paye),

    path('ajoute/produit/', produitView.produits),  
    path('affiche/produit/', produitView.show),  
    path('edit/produit/<int:id>', produitView.edit),  
    path('update/produit/<int:id>', produitView.update),  
    path('delete/produit/<int:id>', produitView.destroy),
    path('produits/search', produitView.search),

    path('ajoute/credit/', creditView.credits),  
    path('affiche/credits/', creditView.show),  
    path('edit/credit/<int:id>', creditView.edit),  
    path('update/credit/<int:id>', creditView.update),  
    path('delete/credit/<int:id>', creditView.destroy),
    path('paye/credit/<int:id>', creditView.paye),
    path('credits/search', creditView.searchClient),


]
