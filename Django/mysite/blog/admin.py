from django.contrib import admin
from .models import Post,Author,Tag,Comment

# username: admin
# password: admin

# Register your models here.

class Postadmin(admin.ModelAdmin):
    prepopulated_fields={"slug":("title",)}
    list_filter=("author","tag","date",)
    list_display=("title","author","date",)
    
class Commentadmin(admin.ModelAdmin):
    list_display=("user_name","post",)    
    

admin.site.register(Post,Postadmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment,Commentadmin)