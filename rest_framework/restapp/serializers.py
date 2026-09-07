from rest_framework import serializers
from restapp.models import Category, Menu
from django.core.mail import send_mail
from typing import cast, Dict, Any
from django.conf import settings


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


"""
class SendEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()
    subject = serializers.CharField()
    message = serializers.CharField()

    def send_email(self):
        data = cast(Dict[str, Any], self.validated_data)
        send_mail(
            subject=data["subject"],
            message=data["message"],
            from_email="Zayonsoft <zayonsoftsoftware@gmail.com>",
            recipient_list=[data["email"]],
        )

"""


class SendEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()
    subject = serializers.CharField()
    body = serializers.CharField()
