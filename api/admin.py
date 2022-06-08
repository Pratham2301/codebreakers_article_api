from django.contrib import admin
from .models import Articles
from .models import Authors

admin.site.register(Articles)
admin.site.register(Authors)