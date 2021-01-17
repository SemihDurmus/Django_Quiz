from django.db import models
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class RegisterSerializer(serializers.ModelSerializer):
    # OVERWRITING FIELDS
    email = serializers.EmailField(required=True, validators=[
                                   UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True, required=True, validators=[
                                     validate_password], style={'input_type': 'password'})
    # write_only means user can only see this field when POSTing but not GET
    # read_only is only for GET
    # style is for showing password as ********
    password2 = serializers.CharField(write_only=True, required=True, style={
                                      'input_type': 'password'})

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password",
            "password2"
        )

    def validate(self, attrs):  # attrs is not a fixed expression
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Password didn't match"}
            )
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"]
        )

        user.set_password(validated_data["password"])
        user.save()

        return user
