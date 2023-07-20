from django.db import models


# Create your models here
# choose Product Type to choose Product Attribute
class ProductType(models.Model):
    title = models.CharField(max_length=32, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Product Type"
        verbose_name_plural = "Product Types"

    def __str__(self):
        return self.title


# each Product has specific Product attribute
class ProductAttribute(models.Model):
    INTEGER = 1
    STRING = 2
    FLOAT = 3

    ATTRIBUTE_TYPES_FIELD = (
        (INTEGER, "Integer"),
        (STRING, "String"),
        (FLOAT, "Float"),
    )
    title = models.CharField(max_length=32)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE, related_name="attributes")
    attribute_type = models.PositiveSmallIntegerField(default=INTEGER, choices=ATTRIBUTE_TYPES_FIELD)

# title that shows in Panel Admin:
    def __str__(self):
        return self.title


# each product may have own Category
class Category(models.Model):
    name = models.CharField(max_length=32)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', null=True, blank=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


# each product may have own Brand
class Brand(models.Model):
    name = models.CharField(max_length=32)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', null=True, blank=True)

    def __str__(self):
        return self.name


# each Product has specific attributes
class Product(models.Model):
    product_type = models.ForeignKey(ProductType, on_delete=models.PROTECT, related_name='products_types')
    upc = models.BigIntegerField(unique=True)
    title = models.CharField(max_length=32)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products_cats')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products_brands')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


# the value of each product attribute
class ProductAttributes(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='attribute_values')
    value = models.CharField(max_length=48)
    attribute = models.ForeignKey(ProductAttribute, on_delete=models.PROTECT, related_name='attribute_values')

    def __str__(self):
        return f"{self.product}({self.attribute}): {self.value}"
