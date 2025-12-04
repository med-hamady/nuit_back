from rest_framework import serializers
from django.contrib.auth import authenticate
from api.models.models import NewUser


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)
    password_confirm = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = NewUser
        fields = ['username', 'email', 'password', 'password_confirm', 'first_name', 'last_name', 'telephone']

    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError({"password": "Les mots de passe ne correspondent pas"})
        return data

    def create(self, validated_data):
        validated_data.pop('password_confirm')
        user = NewUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            telephone=validated_data['telephone']
        )
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if not user.is_active:
                    raise serializers.ValidationError("Ce compte est désactivé")
                data['user'] = user
            else:
                raise serializers.ValidationError("Nom d'utilisateur ou mot de passe incorrect")
        else:
            raise serializers.ValidationError("Nom d'utilisateur et mot de passe requis")

        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'telephone',
                  'is_staff', 'is_active', 'date_joined', 'last_login']
        read_only_fields = ['id', 'date_joined', 'last_login']
