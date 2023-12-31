"""
URL configuration for nft_ecommerce_store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/', include('profile_app.urls')),
    path('', include('store_app.urls', namespace='store')),
    path('cart/', include('cart_app.urls', namespace='cart')),
    path('accounts/', include('allauth.urls')),
]

# handler403 = "board_app.views.access_denied"
# handler400 = "board_app.views.bad_request"
# handler404 = "board_app.views.page_not_found_view"
# handler500 = "board_app.views.handler500"

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
