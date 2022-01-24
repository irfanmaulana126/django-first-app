from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.urls import reverse_lazy, reverse
from django.shortcuts import HttpResponseRedirect
from django.core.exceptions import PermissionDenied

def is_admin_required(func):
    def _function(req, *args, **kwargs):
        if req.user.role is not 1:
            raise PermissionDenied
        return func(req, *args, **kwargs)
    return _function

def is_verifikator_required(func):
    def _function(req, *args, **kwargs):
        if req.user.role not in [1,2]:
            raise PermissionDenied
        return func(req, *args, **kwargs)
    return _function

def is_unit_required(func):
    def _function(req, *args, **kwargs):
        if req.user.role not in [1,3]:
            raise PermissionDenied
        return func(req, *args, **kwargs)
    return _function

def is_dinkes_required(func):
    def _function(req, *args, **kwargs):
        if req.user.role not in [1,4]:
            raise PermissionDenied
        return func(req, *args, **kwargs)
    return _function