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
from digital_dex_admin_web.versions.v1p0.features.taxable_assessment_roll.create_taxable_assessment_roll.views import create_taxable_assessment_roll_views
from digital_dex_admin_web.versions.v1p0.features.taxable_assessment_roll.delete_taxable_assessment_roll.views import delete_taxable_assessment_roll_views
from digital_dex_admin_web.versions.v1p0.features.taxable_assessment_roll.display_taxable_assessment_roll.views import display_taxable_assessment_roll_views
from digital_dex_admin_web.versions.v1p0.features.taxable_assessment_roll.update_taxable_assessment_roll.views import update_taxable_assessment_roll_views


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path("login/", login_view.LoginAdminView.as_view()),
    re_path("logout/", logout_view.LogoutAdminView.as_view()),
    re_path("register/", register_views.RegisterAdminView.as_view()),
    re_path("taxable-assessment-roll/add/", create_taxable_assessment_roll_views.CreateTaxableAssessmentRollView.as_view()),
    re_path("taxable-assessment-roll/delete/", delete_taxable_assessment_roll_views.DeleteTaxableAssessmentRollViews.as_view()),
    re_path("taxable-assessment-roll/update/", update_taxable_assessment_roll_views.UpdateTaxAssessmentRollView.as_view()),
    re_path("taxable-assessment-roll/", display_taxable_assessment_roll_views.DisplayTaxAssessmentRollViews.as_view()),
]
