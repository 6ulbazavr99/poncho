from rest_framework import serializers

from product.models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'preview', 'products', )

    def get_products(self, obj):
        products = obj.products.all()
        return products


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductListSerializer(ProductSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'preview', 'category', 'vendor')


class ProductProfileSerializer(ProductSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'preview', 'category', 'vendor', 'owner',
                  'discount', 'bulk_discount', 'specifications', 'status')
