from django.contrib import admin
from .models import *



admin.site.register(blogs)
# admin.site.register(comments)
admin.site.register(category)

admin.site.register(tags)
admin.site.register(blogPlusTags)

admin.site.register(newsletterSubscription)
admin.site.register(contactQueries)