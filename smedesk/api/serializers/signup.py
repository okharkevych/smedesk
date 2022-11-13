from rest_framework import serializers


class SignupSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    terms = serializers.BooleanField(required=True)
    password = serializers.CharField(
        max_length=16,
        min_length=8,
        required=True
    )
