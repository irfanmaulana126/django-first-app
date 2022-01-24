from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django_datatables_view.base_datatable_view import BaseDatatableView

from core.decorators import *
from userAuth.models import CustomUser
from regpus.models import RegisFaskes

# Create your views here.
@login_required
def dashboard (req):
    return render(req, 'regpus/users.html')

def needverified (req):
    context = {'active':'active'}
    return render(req, 'regpus/need-verified.html',context)

def verifUser (req):
    return render(req, 'regpus/users.html')

def hasverified (req):
    context = {'active':'active'}
    return render(req, 'regpus/has-verified.html',context)

@method_decorator(login_required, name='dispatch')
class itemListViewUserNeedVerified(BaseDatatableView):
    queryset = CustomUser.objects.filter(is_verified=False)
    columns = ['first_name', 'username','province__name','phone', 'is_verified']
    order_columns = ['first_name', 'username', 'province__name', '', '']
    max_display_length = 500
    def get_initial_queryset(self):
        return CustomUser.objects.filter(something=self.kwargs['something'])


@method_decorator(login_required, name='dispatch')
class itemListViewUserHasVerified(BaseDatatableView):
    queryset = CustomUser.objects.filter(is_verified=True)
    columns = ['first_name', 'username','province__name','phone', 'is_verified']