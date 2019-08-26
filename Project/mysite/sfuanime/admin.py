from django.contrib import admin
from .models import MyModel
from .models import Posts
from .models import ModelFoo
from django_summernote.admin import SummernoteModelAdmin


admin.site.register(MyModel)

admin.site.register(ModelFoo)

class PostsAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
admin.site.register(Posts, PostsAdmin)

# Register your models here.
