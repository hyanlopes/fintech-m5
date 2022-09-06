from rest_framework.serializers import ModelSerializer

from users.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        read_only = ["id", "is_superuser", "created_at", "updated_at"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
