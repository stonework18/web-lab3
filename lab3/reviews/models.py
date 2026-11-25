from django.db import models

class Review(models.Model):
    product_name = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    rating = models.IntegerField()
    text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    useful_count = models.IntegerField(default=0)
    # В таблице будет отображаться продукт и имя
    def __str__(self):
        return f"{self.product_name} - {self.author}" 
    class Meta:
        verbose_name = 'Отзыв' # Наименование в ед. числе
        verbose_name_plural = 'Отзывы' # Наименование в мн. числе
        ordering = ['-created_at'] # Сортируем сначала новые