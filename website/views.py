from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib import messages
from django.shortcuts import redirect


from django_role_permissions_poc.roles import Visitor, Buyer, Seller, BackendUser

from rolepermissions.shortcuts \
    import get_user_role, available_perm_status, revoke_permission, grant_permission, remove_role, assign_role

from rolepermissions.decorators import has_permission_decorator, has_role_decorator

from . import models

def index(request):
    template = loader.get_template('website/index.html')
    context = {}
    if request.user.is_authenticated():
        context['role'] = get_user_role(request.user).get_name()
        context['permissions'] = available_perm_status(request.user)
    return HttpResponse(template.render(context, request))

def become_visitor(request, *args, **kwargs):
    if request.user:
        assign_role(request.user, Visitor)
    return redirect('website:index')

@has_role_decorator('visitor')
def become_buyer(request, *args, **kwargs):
    if request.user:
        assign_role(request.user, Buyer)
    return redirect('website:index')

@has_role_decorator('visitor')
def become_seller(request, *args, **kwargs):
    if request.user:
        assign_role(request.user, Seller)
    return redirect('website:index')

@has_permission_decorator('place_bid')
def place_bid(request, *args, **kwargs):
    messages.add_message(request, messages.SUCCESS, 'Bid placed')
    return redirect('website:index')

def modify_bid(request, *args, **kwargs):
    messages.add_message(request, messages.SUCCESS, 'Bid modified')
    return redirect('website:index')

def make_offer(request, *args, **kwargs):
    messages.add_message(request, messages.SUCCESS, 'Offer made')
    return redirect('website:index')

def modify_offer(request, *args, **kwargs):
    messages.add_message(request, messages.SUCCESS, 'offer modified')
    return redirect('website:index')
