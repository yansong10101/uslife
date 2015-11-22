from django.contrib import admin
# from administration.models import USLifeAdmin, USLifeCustomer, University
# from content.models import FeatureGroup, SubFeature, Topic
from django.utils.translation import ugettext_lazy

from django import forms
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

admin.site.site_header = ugettext_lazy('留美帮')
admin.site.site_title = ugettext_lazy('留美帮')


class UniversityAdmin(admin.ModelAdmin):
    list_display = ('org_name', 'created_date', 'modified_date', )


class USLifeAdminAdmin(admin.ModelAdmin):
    list_display = ('username', 'org', )


class USLifeCustomerAdmin(admin.ModelAdmin):
    list_display = ('username', 'org', )


class FeatureGroupAdmin(admin.ModelAdmin):
    list_display = ('feature_name', )


class SubFeatureAdmin(admin.ModelAdmin):
    list_display = ('sub_feature_name', 'feature_group', )


# class TopicAdmin(admin.ModelAdmin):
#     list_display = ('topic_subject', 'created_date', 'modified_date', 'org', 'feature_group', 'sub_feature', )
#
#     def get_queryset(self, request):
#         qs = super(TopicAdmin, self).get_queryset(request)
#         if request.user.is_superuser:
#             return qs
#         admin_user = USLifeAdmin.objects.get(pk=request.user.pk)
#         return qs.filter(org=admin_user.org)
#
#     def save_model(self, request, obj, form, change):
#         if not change:
#             admin_user = USLifeAdmin.objects.get(pk=request.user.pk)
#             obj.org = admin_user.org or None
#         obj.save()


# class SubAdminAccountAdmin(admin.ModelAdmin):
#     list_display = ('username', 'org', )
#
#     def get_queryset(self, request):
#         qs = super(SubAdminAccountAdmin, self).get_queryset(request)
#         if request.user.is_superuser:
#             return qs
#         admin_user = USLifeAdmin.objects.get(pk=request.user.pk)
#         return qs.filter(org=admin_user.org)
#
#     def save_model(self, request, obj, form, change):
#         if not change:
#             admin_user = USLifeAdmin.objects.get(pk=request.user.pk)
#             obj.org = admin_user.org or None
#         obj.save()


# admin.site.register(University, UniversityAdmin)
# admin.site.register(USLifeAdmin, USLifeAdminAdmin)
# admin.site.register(USLifeCustomer, USLifeCustomerAdmin)
#
# admin.site.register(FeatureGroup, FeatureGroupAdmin)
# admin.site.register(SubFeature, SubFeatureAdmin)
# admin.site.register(Topic, TopicAdmin)
# admin.site.register(USLifeSubAdmin, SubAdminAccountAdmin)


# class UserCreationForm(forms.ModelForm):
#     """A form for creating new users. Includes all the required
#     fields, plus a repeated password."""
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
#
#     class Meta:
#         model = MyUser
#         fields = ('email', 'date_of_birth')
#
#     def clean_password2(self):
#         # Check that the two password entries match
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError("Passwords don't match")
#         return password2
#
#     def save(self, commit=True):
#         # Save the provided password in hashed format
#         user = super(UserCreationForm, self).save(commit=False)
#         user.set_password(self.cleaned_data["password1"])
#         if commit:
#             user.save()
#         return user
#
#
# class UserChangeForm(forms.ModelForm):
#     """A form for updating users. Includes all the fields on
#     the user, but replaces the password field with admin's
#     password hash display field.
#     """
#     password = ReadOnlyPasswordHashField()
#
#     class Meta:
#         model = MyUser
#         fields = ('email', 'password', 'date_of_birth', 'is_active', 'is_admin')
#
#     def clean_password(self):
#         # Regardless of what the user provides, return the initial value.
#         # This is done here, rather than on the field, because the
#         # field does not have access to the initial value
#         return self.initial["password"]
#
#
# class MyUserAdmin(UserAdmin):
#     # The forms to add and change user instances
#     form = UserChangeForm
#     add_form = UserCreationForm
#
#     # The fields to be used in displaying the User model.
#     # These override the definitions on the base UserAdmin
#     # that reference specific fields on auth.User.
#     list_display = ('email', 'date_of_birth', 'is_admin')
#     list_filter = ('is_admin',)
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         ('Personal info', {'fields': ('date_of_birth',)}),
#         ('Permissions', {'fields': ('is_admin',)}),
#     )
#     # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
#     # overrides get_fieldsets to use this attribute when creating a user.
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'date_of_birth', 'password1', 'password2')}
#         ),
#     )
#     search_fields = ('email',)
#     ordering = ('email',)
#     filter_horizontal = ()
#
# # Now register the new UserAdmin...
# admin.site.register(MyUser, MyUserAdmin)