from django.db import models

class BookCategory(models.Model):
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="category_bookCategory")
    book = models.ForeignKey("Book", on_delete=models.CASCADE, related_name="bookCategory")
    date = models.DateField(auto_now_add=True)
