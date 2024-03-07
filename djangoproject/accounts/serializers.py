from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'first_name', 'last_name', 'gender','phone_number')


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {
            'password': {'required': True}
        }

    def validate(self, attrs):
        phone_number = attrs.get('phone_number', '').strip().lower()
        if CustomUser.objects.filter(phone_number=phone_number).exists():
            raise serializers.ValidationError('User with this phone number already exists.')
        return attrs

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user


class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'phone_number', 'gender', 'password')

    def update(self, instance, validated_data):
        password = validated_data.pop('password')
        if password:
            instance.set_password(password)
        instance = super().update(instance, validated_data)
        return instance


class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField()  # Replace with serializers.CharField if needed
    password = serializers.CharField(style={'input_type': 'password'}, trim_whitespace=False)

    def validate(self, attrs):
        phone_number = attrs.get('phone_number')  # Replace with your actual field name
        password = attrs.get('password')

        if not phone_number or not password:
            raise serializers.ValidationError("Please provide both phone number and password.")

        # Modify this part based on your actual model and field name
        if not CustomUser.objects.filter(phone_number=phone_number).exists():
            raise serializers.ValidationError('Phone number does not exist.')

        user = authenticate(request=self.context.get('request'), phone_number=phone_number,
                            password=password)
        if not user:
            raise serializers.ValidationError("Wrong Credentials.")

        attrs['user'] = user
        return attrs





