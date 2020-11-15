from django.contrib import admin
from drf_study_code_reviews import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'nickname',
        'date_joined',
    )

    list_display_links = (
        'email',
        'nickname',
    )
