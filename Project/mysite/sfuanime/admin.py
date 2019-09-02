from django.contrib import admin
from .models import MyModel
from .models import Posts
from .models import ModelFoo
from django_summernote.admin import SummernoteModelAdmin

<<<<<<< HEAD
from .models import Posts


admin.site.register(Posts)
=======

admin.site.register(MyModel)

admin.site.register(ModelFoo)

class PostsAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
admin.site.register(Posts, PostsAdmin)
>>>>>>> 73f157eac73a6ce53f5775d16b5e182438dd4a21

# Register your models here.
