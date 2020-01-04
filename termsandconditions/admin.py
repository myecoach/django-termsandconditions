"""Django Admin Site configuration"""

# pylint: disable=R0904
from django import forms
from django.contrib import admin
from django.utils.translation import gettext as _

from .models import TermsAndConditions, UserTermsAndConditions

from ckeditor.widgets import CKEditorWidget


class TermsAndConditionsAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())
    info = forms.CharField(widget=CKEditorWidget(), required=False)

    class Meta:
        fields = (
            'slug',
            'name',
            'version_number',
            'text',
            'info',
            'date_active'
        )
        model = TermsAndConditions


class TermsAndConditionsAdmin(admin.ModelAdmin):
    """Sets up the custom Terms and Conditions admin display"""

    list_display = (
        "slug",
        "name",
        "date_active",
        "version_number",
    )
    verbose_name = _("Terms and Conditions")
    form = TermsAndConditionsAdminForm


class UserTermsAndConditionsAdmin(admin.ModelAdmin):
    """Sets up the custom User Terms and Conditions admin display"""

    # fields = ('terms', 'user', 'date_accepted', 'ip_address',)
    readonly_fields = ("date_accepted",)
    list_display = (
        "terms",
        "user",
        "date_accepted",
        "ip_address",
    )
    date_hierarchy = "date_accepted"
    list_select_related = True


admin.site.register(TermsAndConditions, TermsAndConditionsAdmin)
admin.site.register(UserTermsAndConditions, UserTermsAndConditionsAdmin)
