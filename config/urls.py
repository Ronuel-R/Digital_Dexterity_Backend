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
from digital_dex_admin_web.versions.v1p0.features.registration.views import register_views
from digital_dex_admin_web.versions.v1p0.features.login.views import login_view , logout_view
from digital_dex_admin_web.versions.v1p0.features.ownership_record_card.create_ownership_record.views import create_ownership_record
from digital_dex_admin_web.versions.v1p0.features.ownership_record_card.display_ownership_record_card.views import display_ownership_record_card_view
from digital_dex_admin_web.versions.v1p0.features.ownership_record_card.update_ownership_record_card.views import update_ownership_record_card_view
from digital_dex_admin_web.versions.v1p0.features.ownership_record_card.delete_ownership_record_card.views import delete_ownership_record_card_view

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path("register/", register_views.RegisterAdminView.as_view()),
    re_path("login/", login_view.LoginAdminView.as_view()),
    re_path("logout/", logout_view.LogoutAdminView.as_view()),
    re_path("ownership-record/add/", create_ownership_record.OwnershipRecordCardView.as_view()),
    re_path("ownership-record/delete/", delete_ownership_record_card_view.DeleteOwnershipRecordCardViews.as_view()),
    re_path("ownership-record/update/", update_ownership_record_card_view.UpdateOwnershipRecordCardView.as_view()),
    re_path("ownership-record/", display_ownership_record_card_view.DisplayOwnershipRecordCardViews.as_view()),
]

