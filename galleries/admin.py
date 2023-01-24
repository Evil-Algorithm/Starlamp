from django.contrib import admin

# Register your models here.
from .models import Contact, About, Gallery, Subgalleries

admin.site.register([Contact, About, Gallery, Subgalleries])
