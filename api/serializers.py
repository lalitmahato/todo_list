from rest_framework import serializers
from tasks.models import Task
from users.models import CustomUser

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "first_name", "last_name", "date_of_birth", "gender", "photo", "phone_number", "address", "bio"]


class TaskSerializer(serializers.ModelSerializer):
    creator = UserDetailSerializer(read_only=True)
    modifier = UserDetailSerializer(read_only=True)
    assign_to = UserDetailSerializer(read_only=True)
    class Meta:
        model = Task
        fields = ['id', 'title', 'completed', 'created_at', 'creator', 'modifier', 'assign_to']

    def validate(self, attrs):
        if len(attrs["title"]) < 5:
            raise serializers.ValidationError(
                {"title":"Title must contain at least 5 character!"}
            )
        return attrs

    # def validate_title(self, value):
    #     if len(value) < 5:
    #         raise serializers.ValidationError("Title must contain at least 5 character!")
    #     return value
