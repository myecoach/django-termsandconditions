"""Django Admin Site configuration"""

# pylint: disable=R0904

from django import forms
from django.contrib import admin
from django.utils.translation import gettext as _

from ckeditor.widgets import CKEditorWidget

from .models import TermsAndConditions, UserTermsAndConditions


class TermsAndConditionsAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())
    info = forms.CharField(widget=CKEditorWidget())
    class Meta:
        fields = (
            'slug',
            'name',
            'version_number',
            'type',
            'text',
            'info',
            'date_active'
        )
        model = TermsAndConditions


class TermsAndConditionsAdmin(admin.ModelAdmin):
    """Sets up the custom Terms and Conditions admin display"""
    list_display = ('slug', 'name', 'type', 'date_active', 'version_number',)
    list_filter = ('type',)
    verbose_name = _("Terms and Conditions")
    form = TermsAndConditionsAdminForm


class UserTermsAndConditionsAdmin(admin.ModelAdmin):
    """Sets up the custom User Terms and Conditions admin display"""
    # fields = ('terms', 'user', 'date_accepted', 'ip_address',)
    readonly_fields = ('date_accepted',)
    list_display = ('terms', 'user', 'date_accepted', 'ip_address',)
    date_hierarchy = 'date_accepted'
    list_select_related = True


admin.site.register(TermsAndConditions, TermsAndConditionsAdmin)
admin.site.register(UserTermsAndConditions, UserTermsAndConditionsAdmin)
