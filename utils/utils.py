from django.shortcuts import redirect


def login_excluded(redirect_to):
    #decorator para tirar usuasrios autenticados de uma view
    def _method_wrapper(view_method):
        def _arguments_wrapper(request, *args, **kwargs):
            if request.user.is_authenticated:
                return redirect(redirect_to) 
            return view_method(request, *args, **kwargs)
        return _arguments_wrapper
    return _method_wrapper

def checar_repeticao(lista1, lista2):
    result = False
 
    for x in lista1:
 
        for y in lista2:
   
            if x == y:
                result = True
                return result
                 
    return result