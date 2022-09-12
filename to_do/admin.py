from django.contrib import admin
from .models import ToDoList
from django.utils.html import format_html
from django.db import models
class ToDoAdmin(admin.ModelAdmin):
    list_display = ('id_link', 'item', 'completed',)
    change_list_template = 'admin/to_do/change_list.html'
    list_display_links = None
    editable_objs = []
    def id_link(self, obj):
        if obj in self.editable_objs:
            return format_html("<a href='{id}'>{id}</a>",
                               id=obj.id,
                               )
        else:
            return format_html("{id}",
                               id=obj.id,
                               )
    id_link.short_description = 'ID'
    id_link.allow_tags = True
    id_link.admin_order_field = '_id_link'
    def get_queryset(self, request):
        self.editable_objs = ToDoList.objects.filter(user=request.user)
        return super(ToDoAdmin, self).get_queryset(
            request,
        ).annotate(_id_link=models.Count('id'))
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