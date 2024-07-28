from django.contrib import admin
from .models import AdminProfile

@admin.register(AdminProfile)
class AdminProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'profile_picture', 'cv')
    search_fields = ('user__username',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs.filter(user=request.user)
        return qs.filter(user=request.user) 

    def has_change_permission(self, request, obj=None):
        if obj is not None:
            return obj.user == request.user
        return super().has_change_permission(request, obj)

    def has_view_permission(self, request, obj=None):
        if obj is not None:
            return obj.user == request.user
        return super().has_view_permission(request, obj)
