from django.db import models

class BookReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="books_category")
    book = models.ForeignKey("book", on_delete=models.CASCADE, related_name="bookCategory")