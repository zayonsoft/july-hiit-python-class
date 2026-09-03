from rest_framework import serializers
from restapp.models import Category, Menu


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class MenuSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        source="category", write_only=True, queryset=Category.objects.all()
    )

    class Meta:
        model = Menu
        fields = "__all__"
