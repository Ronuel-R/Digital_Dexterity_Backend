"""Digital_Dex_Backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,re_path
from digital_dex_admin_web.versions.v1p0.features.login.views import login_view
from digital_dex_admin_web.versions.v1p0.features.registration.views import register_views
from digital_dex_admin_web.versions.v1p0.features.tax_map_control.create_tax_map_control.views import create_tax_map_control_views
from digital_dex_admin_web.versions.v1p0.features.tax_map_control.update_tax_map_control.views import update_tax_map_control_views
from digital_dex_admin_web.versions.v1p0.features.tax_map_control.delete_tax_map_control.views import delete_tax_map_control_views
from digital_dex_admin_web.versions.v1p0.features.tax_map_control.display_tax_map_control.views import display_tax_map_control_views


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path("login/", login_view.LoginAdminView.as_view()),
    re_path("logout/", login_view.LogoutAdminView.as_view()),
    re_path("register/", register_views.RegisterAdminView.as_view()),
    re_path("tax-map-control/add/", create_tax_map_control_views.CreateTaxMapControlViews.as_view()),
    re_path("tax-map-control/update/", update_tax_map_control_views.UpdateTaxMapControl.as_view()),
    re_path("tax-map-control/delete/", delete_tax_map_control_views.DeleteTaxMapControlViews.as_view()),
    re_path("tax-map-control/", display_tax_map_control_views.DisplayTaxMapControlViews.as_view()),
    
]

