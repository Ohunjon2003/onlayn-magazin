from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Post,Category,UserProfile,Comment
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('id','name','content','created','update','views','category','published','get_photo')
    list_display_links = ('name',)
    list_editable = ('published','category')
    list_filter = ('published','category')
    search_fields = ('name','content')
    def get_photo(self,obj):
        return mark_safe(f'<img src="{obj.photo.url if obj.photo else None}" width="75">')


admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(UserProfile)
admin.site.register(Comment)