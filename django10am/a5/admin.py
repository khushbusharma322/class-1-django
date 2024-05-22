from django.contrib import admin
from .models import Book
# Register your models here.
class Bookdisplay(admin.ModelAdmin):
    list_display=["id","bname","authorname","price"]
admin.site.register(Book,Bookdisplay)