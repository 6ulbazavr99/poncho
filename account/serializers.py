from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from account.models import Vendor
from product.models import Product
from product.serializers import ProductSerializer, CategorySerializer

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()
    vendors = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = '__all__'

    def get_products(self, obj):
        user_id = self.context['request'].user.id
        products = Product.objects.filter(owner=user_id)
        serialized_data = ProductSerializer(products, many=True).data
        products_info = [{'id': product_data.get('id'), 'title': product_data.get('title')} for product_data in
                         serialized_data]
        return products_info

    def get_vendors(self, obj):
        user_id = self.context['request'].user.id
        vendors = Vendor.objects.filter(members=user_id)
        serialized_data = VendorSerializer(vendors, many=True).data
        vendors_info = [{'id': vendor_data.get('id'), 'name': vendor_data.get('name')} for vendor_data in
                        serialized_data]
        return vendors_info


class UserProfileSerializer(UserSerializer):

    class Meta:
        model = User
        # fields = ('id', 'username', 'email', 'first_name', 'last_name', 'avatar', 'birthdate', 'products', 'vendors')
        fields = '__all__'


class UserListSerializer(UserSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'is_active', 'is_superuser', 'products', 'vendors')


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, max_length=32,
                                     required=True, write_only=True)
    password2 = serializers.CharField(min_length=8, max_length=32,
                                      required=True, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2',
                  'first_name', 'last_name', 'avatar', 'birthdate')

    def validate(self, attrs):
        password = attrs['password']
        password2 = attrs.pop('password2')
        if password2 != password:
            raise serializers.ValidationError('Пароли не совпадают')
        validate_password(password)
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class VendorSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()
    categories = serializers.SerializerMethodField()

    class Meta:
        model = Vendor
        fields = '__all__'

    def get_products(self, obj):
        products = Product.objects.filter(vendor=obj)
        serialized_data = ProductSerializer(products, many=True).data
        products_info = [{'id': product_data.get('id'), 'title': product_data.get('title')} for product_data in
                         serialized_data]
        return products_info

    def get_categories(self, obj):
        products = obj.products.all()
        categories = [product_category.category for product_category in products]
        categories_serialized_data = CategorySerializer(categories, many=True).data
        categories_info = [{'id': category_data.get('id'), 'name': category_data.get('name')} for category_data in
                           categories_serialized_data]
        return categories_info


class VendorListSerializer(VendorSerializer):

    class Meta:
        model = Vendor
        fields = ('id', 'name', 'avatar', 'description', 'categories', 'products')


class VendorProfileSerializer(VendorSerializer):

    class Meta:
        model = Vendor
        fields = '__all__'