from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def form(request, input_name):
    """la valeur entrée dans l'input du formulaire

    Args:
        request (Request): requête
        input_name (String): le nom de l'input

    Returns:
        String: ...
    """
    return request.POST[input_name]

def utilisateur(request):
    """l'utilisateur qui tente de s'identifier

    Args:
        request (Request): requête

    Returns:
        Object: ...
    """
    return authenticate(request, username=form(request, "nom_utilisateur"), password=form(request, "mot_de_passe"))

def utilisateur_existe(request):
    """est-ce l'utilisateur est bien enregistré en BDD ?

    Args:
        request (Request): requête

    Returns:
        Boolean: ...
    """
    return utilisateur(request) is not None

def index(request):
    if request.method == "POST":
        if utilisateur_existe(request):
            login(request, utilisateur(request)) # on se connecte
            
            return redirect("dashboard")
        return render(request, "login.html", {})
    else:
        return render(request, "login.html", {})

def logout_utilisateur(request):
    logout(request) # on se déconnecte

    return redirect("login") # on est redirigé vers la page de login
