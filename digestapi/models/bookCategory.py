from django.db import models

class BookCategory(models.Model):
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    book = models.ForeignKey("Book", on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
