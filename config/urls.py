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
from digital_dex_admin_web.versions.v1p0.features.exempt_assessment_roll.create_exempt_assessment.views import exempt_assessment_view
from digital_dex_admin_web.versions.v1p0.features.exempt_assessment_roll.display_exempt_assessment.views import display_exempt_assessment_views
from digital_dex_admin_web.versions.v1p0.features.exempt_assessment_roll.update_exempt_assessment_roll.views import update_exempt_assessment_roll_view
from digital_dex_admin_web.versions.v1p0.features.exempt_assessment_roll.delete_exempt_assessment.views import delete_exempt_assessment_roll


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path("login/", login_view.LoginAdminView.as_view()),
    re_path("logout/", logout_view.LogoutAdminView.as_view()),
    re_path("register/", register_views.RegisterAdminView.as_view()),
    re_path("exempt-assessment-roll/add/", exempt_assessment_view.ExemptAssessmentRollView.as_view()),
    re_path("exempt-assessment-roll/delete/", delete_exempt_assessment_roll.DeleteExemptAssessmentRollViews.as_view()),
    re_path("exempt-assessment-roll/update/", update_exempt_assessment_roll_view.UpdateExemptAssessmentRollView.as_view()),
    re_path("exempt-assessment-roll/", display_exempt_assessment_views.DisplayExemptAssessmentRollViews.as_view()),
]
