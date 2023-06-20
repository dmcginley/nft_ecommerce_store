from django.urls import path
# from . import views


from profile_app .views import (
    ProfileListView
)


urlpatterns = [
    path('', ProfileListView.as_view(), name='profile'),
    # path('', ProfileListView.as_view(), name='profile'),
]
