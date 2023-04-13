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
from digital_dex_admin_web.versions.v1p0.features.login.views import login_view , logout_view
from digital_dex_admin_web.versions.v1p0.features.registration.views import register_views
from digital_dex_admin_web.versions.v1p0.features.tax_declaration_form.create_tax_form.views import tax_form_views
from digital_dex_admin_web.versions.v1p0.features.tax_declaration_form.display_tax_dec.views import display_tax_views
from digital_dex_admin_web.versions.v1p0.features.tax_declaration_form.delete_tax_dec.views import delete_tax_views
from digital_dex_admin_web.versions.v1p0.features.tax_declaration_form.update_tax_form.views import update_tax_views
from digital_dex_admin_web.versions.v1p0.features.tax_map_control.create_tax_map_control.views import create_tax_map_control_views
from digital_dex_admin_web.versions.v1p0.features.tax_map_control.update_tax_map_control.views import update_tax_map_control_views
from digital_dex_admin_web.versions.v1p0.features.tax_map_control.delete_tax_map_control.views import delete_tax_map_control_views
from digital_dex_admin_web.versions.v1p0.features.tax_map_control.display_tax_map_control.views import display_tax_map_control_views
from digital_dex_admin_web.versions.v1p0.features.taxable_assessment_roll.create_taxable_assessment_roll.views import create_taxable_assessment_roll_views
from digital_dex_admin_web.versions.v1p0.features.taxable_assessment_roll.delete_taxable_assessment_roll.views import delete_taxable_assessment_roll_views
from digital_dex_admin_web.versions.v1p0.features.taxable_assessment_roll.display_taxable_assessment_roll.views import display_taxable_assessment_roll_views
from digital_dex_admin_web.versions.v1p0.features.taxable_assessment_roll.update_taxable_assessment_roll.views import update_taxable_assessment_roll_views
from digital_dex_admin_web.versions.v1p0.features.exempt_assessment_roll.create_exempt_assessment.views import exempt_assessment_view
from digital_dex_admin_web.versions.v1p0.features.exempt_assessment_roll.display_exempt_assessment.views import display_exempt_assessment_views
from digital_dex_admin_web.versions.v1p0.features.exempt_assessment_roll.update_exempt_assessment_roll.views import update_exempt_assessment_roll_view
from digital_dex_admin_web.versions.v1p0.features.exempt_assessment_roll.delete_exempt_assessment.views import delete_exempt_assessment_roll
from digital_dex_admin_web.versions.v1p0.features.ownership_record_card.create_ownership_record.views import create_ownership_record
from digital_dex_admin_web.versions.v1p0.features.ownership_record_card.display_ownership_record_card.views import display_ownership_record_card_view
from digital_dex_admin_web.versions.v1p0.features.ownership_record_card.update_ownership_record_card.views import update_ownership_record_card_view
from digital_dex_admin_web.versions.v1p0.features.ownership_record_card.delete_ownership_record_card.views import delete_ownership_record_card_view

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path("login/", login_view.LoginAdminView.as_view()),
    re_path("logout/", logout_view.LogoutAdminView.as_view()),
    re_path("register/", register_views.RegisterAdminView.as_view()),
    re_path("tax-declaration/add/", tax_form_views.TaxFormViews.as_view(), name='create_tax_dec'),
    re_path("tax-declaration/delete/", delete_tax_views.DeleteTaxDecViews.as_view(), name='delete_tax_dec'),
    re_path("tax-declaration/update/", update_tax_views.UpdateTaxFormViews.as_view(), name='update_tax_dec'),
    re_path("tax-declaration/", display_tax_views.DisplayTaxDecViews.as_view(), name='display_tax_dec'),
    re_path("tax-map-control/add/", create_tax_map_control_views.CreateTaxMapControlViews.as_view()),
    re_path("update-tax-map-control/", update_tax_map_control_views.UpdateTaxMapControl.as_view()),
    re_path("tax-map-control/delete/", delete_tax_map_control_views.DeleteTaxMapControlViews.as_view()),
    re_path("tax-map-control/", display_tax_map_control_views.DisplayTaxMapControlViews.as_view()),
    re_path("taxable-assessment-roll/create/", create_taxable_assessment_roll_views.CreateTaxableAssessmentRollView.as_view()),
    re_path("taxable-assessment-roll/delete/", delete_taxable_assessment_roll_views.DeleteTaxableAssessmentRollViews.as_view()),
    re_path("taxable-assessment-roll/update/", update_taxable_assessment_roll_views.UpdateTaxAssessmentRollView.as_view()),
    re_path("taxable-assessment-roll/", display_taxable_assessment_roll_views.DisplayTaxAssessmentRollViews.as_view()),
    re_path("exempt-assessment-roll/add/", exempt_assessment_view.ExemptAssessmentRollView.as_view()),
    re_path("exempt-assessment-roll/delete/", delete_exempt_assessment_roll.DeleteExemptAssessmentRollViews.as_view()),
    re_path("exempt-assessment-roll/update/", update_exempt_assessment_roll_view.UpdateExemptAssessmentRollView.as_view()),
    re_path("exempt-assessment-roll/", display_exempt_assessment_views.DisplayExemptAssessmentRollViews.as_view()),
    re_path("ownership-record/add/", create_ownership_record.OwnershipRecordCardView.as_view()),
    re_path("ownership-record/delete/", delete_ownership_record_card_view.DeleteOwnershipRecordCardViews.as_view()),
    re_path("ownership-record/update/", update_ownership_record_card_view.UpdateOwnershipRecordCardView.as_view()),
    re_path("ownership-record/", display_ownership_record_card_view.DisplayOwnershipRecordCardViews.as_view()),
]




    


