from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Note, Profile

class RegisterSerializer(serializers.ModelSerializer):
    address = serializers.CharField(required=False, allow_blank=True)
    phone_number = serializers.CharField(required=False, allow_blank=True)
    secondary_email = serializers.EmailField(required=False, allow_blank=True)

    class Meta:
        model = User
        fields = ["id", "email", "password", "address", "phone_number", "secondary_email"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        address = validated_data.pop("address", "")
        phone_number = validated_data.pop("phone_number", "")
        secondary_email = validated_data.pop("secondary_email", "")
        email = validated_data.get("email")

        base = email.split("@")[0]
        username = base
        counter = 1
        while User.objects.filter(username=username).exists():
            username = f"{base}{counter}"
            counter += 1

        user = User.objects.create_user(username=username, **validated_data)
        Profile.objects.create(
            user=user,
            address=address,
            phone_number=phone_number,
            secondary_email=secondary_email
        )
        return user

class EmailTokenObtainPairSerializer(TokenObtainPairSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop("username", None)
        self.fields["email"] = serializers.EmailField()

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        if email and password:
            user = None
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                try:
                    profile = Profile.objects.get(secondary_email=email)
                    user = profile.user
                except Profile.DoesNotExist:
                    raise serializers.ValidationError("No active account found with the given credentials")

            user = authenticate(username=user.username, password=password)
            if not user or not user.is_active:
                raise serializers.ValidationError("No active account found with the given credentials")

            refresh = RefreshToken.for_user(user)
            return {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }

        raise serializers.ValidationError("Must include 'email' and 'password'")

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "content", "created_at", "completed", "author"]
        extra_kwargs = {"author": {"read_only": True}}
