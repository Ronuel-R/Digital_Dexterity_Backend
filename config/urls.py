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
from digital_dex_admin_web.versions.v1p0.features.create_tax_form.views import tax_form_views
from digital_dex_admin_web.versions.v1p0.features.display_tax_dec.views import display_tax_views
from digital_dex_admin_web.versions.v1p0.features.delete_tax_dec.views import delete_tax_views
from digital_dex_admin_web.versions.v1p0.features.update_tax_form.views import update_tax_views
from digital_dex_admin_web.versions.v1p0.features.login.views import login_view , logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path("login/", login_view.LoginAdminView.as_view()),
    re_path("logout/", logout_view.LogoutAdminView.as_view()),
    re_path("register/", register_views.RegisterAdminView.as_view()),
    re_path("tax-declaration/add/", tax_form_views.TaxFormViews.as_view(), name='create_tax_dec'),
    re_path("tax-declaration/delete/", delete_tax_views.DeleteTaxDecViews.as_view(), name='delete_tax_dec'),
    re_path("tax-declaration/update/", update_tax_views.UpdateTaxFormViews.as_view(), name='update_tax_dec'),
    re_path("tax-declaration/", display_tax_views.DisplayTaxDecViews.as_view(), name='display_tax_dec'),
]
