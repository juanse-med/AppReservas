
from django.contrib.auth.decorators import login_required, user_passes_test

def es_administrador(user):
    return user.groups.filter(name='Administradores').exists()

def administrador_required(view_func):
    decorated_view_func = login_required(user_passes_test(es_administrador))
    return decorated_view_func
