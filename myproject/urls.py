"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
# myproject/urls.py
from django.contrib import admin
from django.urls import path
from myapp.views import add_product,product_list, update_product
from myapp.views import user_login
from myapp.views import signup
from myapp.views import logout_view
from myapp.views import delete_product

urlpatterns = [
    path('product_list/', product_list, name='product_list'),
    path('add_product', add_product, name='add_product'),
    path('delete_product/<int:product_id>/', delete_product, name='delete_product'),
    path('update_product/<int:product_id>/', update_product, name='update_product'),
    path('admin/', admin.site.urls),
    path('login/', user_login, name='user_login'),
    path('', signup, name='signup'),
    path('logout/', logout_view, name='logout')
]