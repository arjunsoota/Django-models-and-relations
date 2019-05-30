from django.contrib import admin
from relationship_playground import models
# Register your models here.

admin.site.register(
    [
        models.article,
        models.author,
        models.Pizza,
        models.Topping,
        models.Person,
        models.Society,
        models.Membership
    ]
)