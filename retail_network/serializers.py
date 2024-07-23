from rest_framework import serializers

from retail_network.models import Network


class NetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Network
        fields = '__all__'
        read_only_fields = ['debt_to_supplier']  # Запрет на обновление поля "Задолженность перед поставщиком" через API
