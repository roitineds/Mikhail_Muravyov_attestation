from django.db import models


class Product(models.Model):
    """
    Модель для представления продукта.
    """

    title = models.CharField(max_length=20, verbose_name="название")
    model = models.CharField(max_length=50, verbose_name="модель")
    release_date = models.DateField(verbose_name="дата выхода на рынок")

    def __str__(self):
        """
        Возвращает строковое представление объекта Product.
        """
        return f"{self.title} - {self.model}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"