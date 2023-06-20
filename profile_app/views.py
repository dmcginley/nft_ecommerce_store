from django.shortcuts import render
from store_app.models import Product
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import (
    ListView,
)


class ProfileListView(LoginRequiredMixin, ListView):
    model = Profile
    username = User.username
    template_name = 'profile_app/profile_page.html'
    context_object_name = 'posts'
