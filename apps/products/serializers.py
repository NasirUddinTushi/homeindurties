from rest_framework import serializers
from .models import Product, Category, Attribute, AttributeValue, ProductImage

class AttributeValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttributeValue
        fields = ['id', 'value']

class AttributeSerializer(serializers.ModelSerializer):
    attribute_id = serializers.IntegerField(source='id')
    attribute_name = serializers.CharField(source='name')
    attribute_value = serializers.SerializerMethodField()

    class Meta:
        model = Attribute
        fields = ['attribute_id', 'attribute_name', 'attribute_value']

    def get_attribute_value(self, obj):
        
        values = obj.values.all()
        return [v.value for v in values]  
        

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['image']

class ProductSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    attribute_id = serializers.SerializerMethodField()
    category_id = serializers.IntegerField(source='category.id', read_only=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "slug",
            "category_id",
            "is_bestseller",
            "is_new",
            "price",
            "sale_price",
            "short_description",
            "images",
            "attribute_id",
        ]

    def get_images(self, obj):
        
        return [img.image.url for img in obj.images.all()]

    def get_attribute_id(self, obj):
       
        return list(obj.attributes.all().values_list("id", flat=True))
class CategorySerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(source='id')
    category_name = serializers.CharField(source='name')
    category_slug = serializers.CharField(source='slug')
    parent_category_id = serializers.IntegerField(source='parent.id', allow_null=True)
    
    # Custom fields
    show_in_footer = serializers.SerializerMethodField()
    category_image_url = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = [
            'category_id',
            'parent_category_id',
            'category_name',
            'category_slug',
            'category_image_url',
            'show_in_footer',
        ]

    def get_show_in_footer(self, obj):
        # Default value for show_in_footer (can be customized as per need)
        return 0

    def get_category_image_url(self, obj):
        # If there is an image associated with the category, return its URL
        if obj.image:
            return obj.image.url
        return ""  # If no image, return an empty string