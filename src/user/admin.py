from django.contrib import admin

from .models import (
    MainModule,
    PermissionCategory,
    User,
    UserGroup,
    UserPermission,
)

admin.site.register(User)
admin.site.register(UserGroup)
admin.site.register(UserPermission)
admin.site.register(PermissionCategory)
admin.site.register(MainModule)
