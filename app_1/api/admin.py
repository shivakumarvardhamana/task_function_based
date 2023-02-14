from django.contrib import admin

from .models import likes,blog
# admin.site.register(likes)
# admin.site.register(blog)

@admin.register(likes)
class a(admin.ModelAdmin):
    list_display=['id','likes_total_count']
@admin.register(blog)
class b(admin.ModelAdmin):
    list_display=['id','user','likes_total_count','caption','article']