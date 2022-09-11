from django.contrib import admin
from .models import ToDoList
from django.contrib import messages
from django import forms
# class ToDoAdminForm(forms.ModelForm):
#     class Meta:
#         model = ToDoList
#         fields = '__all__'

#     def clean(self):
#         raise forms.ValidationError({'user': "User Mismatch"})

class ToDoAdmin(admin.ModelAdmin):
    list_display = ('id', 'item', 'completed',)

    def changelist_view(self, request, extra_context=None):

        print(request.user)
        print(extra_context)
        # if self.user:
        #     self.list_display = ('name', )
        #     # if you dont want any links to the change_form
        self.list_display_links = None
        return super(ToDoAdmin, self).changelist_view(request, extra_context)

    def get_form(self, request, obj=None, **kwargs):
        form = super(ToDoAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['user'].initial = request.user
        form.base_fields['user'].disabled = True
        form.base_fields['user'].help_text = "This field is not editable"
        if obj and obj.user != request.user:
            form.base_fields['completed'].disabled = True
            form.base_fields['item'].disabled = True
            form.base_fields['completed'].help_text = "This field is not editable"
        return form
admin.site.register(ToDoList,ToDoAdmin)