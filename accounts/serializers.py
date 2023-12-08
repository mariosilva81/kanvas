from rest_framework.serializers import ModelSerializer
from .models import Account
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class AccountSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = ("id", "username", "email", "password", "is_superuser")
        extra_kwargs = {
            "email": {
                "validators": [
                    UniqueValidator(
                        queryset=Account.objects.all(),
                        message="user with this email already exists.",
                    )
                ]
            },
            "password": {"write_only": True},
        }

    def validate_password(self, value):
        validate_password(value, self.instance)
        return value

    def create(self, validated_data: dict) -> Account:
        is_superuser = validated_data.get("is_superuser", False)
        if is_superuser:
            return Account.objects.create_superuser(**validated_data)
        return Account.objects.create_user(**validated_data)
