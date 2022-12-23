from django.contrib import admin

from .models import Article
# .models dosyamızın içinde oluturduğumuz Article modelini importladık çünkü oluşan modeli admin sayfasında görüntülemek istiyoruz
# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display = ["title","author", "created_date"]
    list_display_links = ["title", "created_date"]
    search_fields = ["title"]
    list_filter = ["created_date"]
    class Meta:
      model = Article

