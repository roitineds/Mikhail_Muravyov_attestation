from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .products import Product

NULLABLE = {'null': True, 'blank': True}


class Network(models.Model):
    """
    Модель для представления звена сети.
    """

    LEVEL_CHOICES = (
        (0, 'Завод'),
        (1, 'Розничная сеть'),
        (2, 'Индивидуальный предприниматель'),
    )

    name = models.CharField(max_length=255, verbose_name="название")
    level = models.IntegerField(choices=LEVEL_CHOICES, **NULLABLE)
    email = models.EmailField()
    country = models.CharField(max_length=100, verbose_name="страна")
    city = models.CharField(max_length=100, verbose_name="город")
    street = models.CharField(max_length=100, verbose_name="улица")
    house_number = models.CharField(max_length=10, verbose_name="номер дома")
    products = models.ManyToManyField(Product, related_name='network_nodes', verbose_name="продукты")
    supplier = models.ForeignKey('self', on_delete=models.SET_NULL, **NULLABLE, verbose_name="поставщик")
    debt_to_supplier = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="задолженность")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="дата создания")

    def __str__(self):
        """
        Возвращает строковое представление объекта Network.
        """
        return f"{self.name}, {self.email}, {self.country}"

    class Meta:
        ordering = ["id"]
        verbose_name = "Звено сети"
        verbose_name_plural = "Звенья сети"


@receiver(pre_save, sender=Network)
def set_network_level(sender, instance, **kwargs):
    """
    Обработчик сигнала pre_save, устанавливает уровень (level) объекта Network.
    """
    if instance.supplier:
        instance.level = instance.supplier.level + 1
    else:
        # Если у объекта нет поставщика, он считается заводом (уровень 0)
        instance.level = 0