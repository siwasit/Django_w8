from django.contrib import admin
from .models import Product, ProductComment
from django.contrib.auth.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'date_joined', 'is_staff')  # Show date_joined in the user list
    readonly_fields = ('date_joined', 'last_login')

admin.site.register(Product)
admin.site.register(ProductComment)
admin.site.unregister(User)  # Unregister default User admin
admin.site.register(User, UserAdmin)  # Register custom User admin
