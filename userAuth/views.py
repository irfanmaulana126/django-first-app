from django.core.checks import messages
from django.shortcuts import render, redirect
from .models import CustomUser,Province , Regencies, Villages
from django.contrib.auth import authenticate, get_user_model, logout,login, update_session_auth_hash
from django.http import HttpResponseRedirect, request, JsonResponse
from django.template.loader import get_template, render_to_string
from django.contrib import messages
from django.urls import reverse, reverse_lazy, resolve
from django.contrib.sites.shortcuts import get_current_site
from django.views.generic import CreateView

from .forms import SignUpForm, UserRegistrationForm

# Create your views here.
class Register(CreateView):
    model = CustomUser
    form_class = UserRegistrationForm
    template_name = "userAuth/index_register.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["provinces"] =  Province.objects.filter(is_active=False)
        return context
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()
        current_site = get_current_site(self.request)
        return render(self.request,'userAuth/redirect_verif.html',{"message":False})


def signin (req):
    username = password = ''
    print(req)
    if req.user.is_authenticated:
        return HttpResponseRedirect('/dashboard')
    else:
        if req.POST:
            email = req.POST['email']
            password = req.POST['password']
            user = authenticate(username=email, password=password)
            if user is not None:
                if user.is_verified:
                    login(req, user)
                    return HttpResponseRedirect('/dashboard')
                else:
                    messages.add_message(req, messages.INFO,'Akun Anda belum Terverifikasi oleh pusat')
            else:
                messages.add_message(req, messages.INFO, 'username atau password salah')
    return render(req,"userAuth/index_login.html")

def signout (req):
    logout(req)
    return redirect(reverse('otentik:login'))

def register (req):
    if req.POST:
        pass
    else:
        return render(req,"userAuth/index_register.html")

def getRegencies(request):
    
    if request.POST:
        kab_list = Regencies.objects.filter(id_prov=request.POST["id_prov"], is_active=False)
        listoption = render_to_string('externalhtml/kab_select.html', {
                    'arrs': kab_list,
        })
        # print(listoption)
        r = True
        htmly = listoption
        return JsonResponse({"result":r,"htmly":htmly})
    else:
        r =  False
        return JsonResponse({"result":False,"htmly":''})