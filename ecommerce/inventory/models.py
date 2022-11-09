from django.db import models
from django.utils.translation import  gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField


class Category(MPTTModel):
  
  name = models.CharField(max_length=100, null=False, unique=False, blank=False, verbose_name=_("category name"), help_text=_("format: required, max-100"))
  slug = models.SlugField(max_length=150, null=False, unique=False, blank=False, verbose_name=_("category safe url"), help_text=_("format: required, letters, numbers, underscore, or hyphens"))
  is_active = models.BooleanField(default=True)
  
  parent = TreeForeignKey("self", on_delete=models.PROTECT, null=True, blank=True, unique=False, related_name= "children", verbose_name=_("parent of category"), help_text=_("format: not required"))
  
  class MPTTMeta:
    order_insertion_by = ["name"]
    
  class Meta:
    verbose_name = _("product category")
    verbose_name_plural = _("product categories")
    
  def __str__(self):
    return self.name


class Product(models.Model):
  web_id = models.CharField(max_length=50, unique=True, null=False, blank=False, verbose_name=_("product website ID"), help_text=_("format: required, unique"))
  slug = models.SlugField(max_length=255, unique=False, null=False, blank=False, verbose_name=_("product safe url"), help_text=_("format: required, letters, numbers, underscores of hyphens"))
  name = models.CharField(max_length=255, null=False, unique=False, blank=False, verbose_name=_("product name"), help_text=_("format: required, max-255"))
  description = models.TextField(unique=False, null=False, blank=False, verbose_name=_("product description"), help_text=_("format: required"))
  category = TreeManyToManyField(Category)
  is_active = models.BooleanField(unique=False, null=False, blank=False, default=True, verbose_name=_("product visibility"), help_text=_("format: true=product visibility"))
  created_at = models.DateTimeField(auto_now_add=True, editable=True, verbose_name=_("data product created"), help_text=_("format: Y-m-d H:M:S"))
  updated_at = models.DateTimeField(auto_now=True, verbose_name=_("data product last updated"), help_text=_("format: Y-m-d H:M:S"))
  
  def __str__(self):
    return self.name

class ProductType(models.Model):
  name = models.CharField(max_length=255, null=False, unique=True, blank=False, verbose_name=_("type of product"), help_text=_("format: required, max-255"))

  def __str__(self):
    return self.name

class Brand(models.Model):
  name = models.CharField(max_length=255, null=False, unique=True, blank=False, verbose_name=_("brand name"), help_text=_("format: required, max-255"))
  

class ProductAttribute(models.Model):
  name = models.CharField(max_length=255, unique=True, null=False, blank=False, verbose_name=_("product attribute name"), help_text=_("format: required, unique, max-255"))
  description = models.TextField(unique=False, null=False, blank=False, verbose_name=_("product attribute description"), help_text=_("format: required"))
  
  def __str__(self):
    return self.name


class ProductAttributeValue(models.Model):
  product_attribute = models.ForeignKey(ProductAttribute, related_name="product_attribute", on_delete=models.PROTECT)
  attribute_value = models.CharField(max_length=255, unique=False, null=False, blank=False, verbose_name=_("attribute value"), help_text=_("format: required, max-255"))
  
  def __str__(self):
    return f"{self.product_attribute.name} : {self.attribute_value}"


class ProductInventory(models.Model):
  sku = models.CharField(max_length=50, unique=True, null=False, blank=False, verbose_name=_("stock keeping unit"), help_text=_("format: required, unique, max-50"))
  upc = models.CharField(max_length=15, unique=True, null=False, blank=False, verbose_name=_("universal product code"), help_text=_("format: required, unique, max-15"))
  product_type = models.ForeignKey(ProductType, related_name="product_type", on_delete=models.PROTECT)
  product = models.ForeignKey(Product, related_name="product", on_delete=models.PROTECT)
  brand = models.ForeignKey(Brand, related_name="brand", on_delete=models.PROTECT)
  attribute_values = models.ManyToManyField(ProductAttributeValue, related_name="product_attribute_values", through="ProductAttributeValues")
  is_active = models.BooleanField(default=True, verbose_name=_("product visibility"), help_text=_("format: true=product visibility"))
  retail_price = models.DecimalField(max_digits=5, decimal_places=2, unique=False, null=False, blank=False, verbose_name=_("recommended retail price"), help_text=_("format: maximum price 999.99"), error_messages={"name": {"max_length": _("the price must be between 0 and 999.99."),},},)
  store_price = models.DecimalField(max_digits=5, decimal_places=2, unique=False, null=False, blank=False, verbose_name=_("regular store price"), help_text=_("format: maximum price 999.99"), error_messages={"name": {"max_length": _("the price must be between 0 and 999.99."),},},)
  sale_price = models.DecimalField(max_digits=5, decimal_places=2, unique=False, null=False, blank=False, verbose_name=_("sale price"), help_text=_("format: maximum price 999.99"), error_messages={"name": {"max_length": _("the price must be between 0 and 999.99."),},},)
  weight= models.FloatField(unique=False, null=False, blank=False, verbose_name=_("product weight"))
  created_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name=_("data sub-product created"), help_text=_("format: Y-m-d H:M:S"))
  updated_at = models.DateTimeField(auto_now=True, verbose_name=_("data sub-product updated"), help_text=_("format: Y-m-d H:M:S"))
  
  def __str__(self):
    return self.product.name


class Media(models.Model):
  product_inventory = models.ForeignKey(ProductInventory, on_delete=models.PROTECT, related_name="media_product_inventory")
  image = models.ImageField(unique=False, null=False, blank=False, verbose_name=_("product image"), upload_to="images/", default="images/default.png", help_text=_("format: required, default-default.png"))
  alt_text = models.CharField(max_length=255, unique=False, null=False, blank=False, verbose_name=_("alternative text"), help_text=_("format: required, max-255"))
  is_feature = models.BooleanField(default=False, verbose_name=_("product default image"), help_text=_("format: default=false, true=default image"))
  created_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name=_("data sub-product created"), help_text=_("format: Y-m-d H:M:S"))
  updated_at = models.DateTimeField(auto_now=True, verbose_name=_("data sub-product updated"), help_text=_("format: Y-m-d H:M:S"))
  
  class Meta:
    verbose_name = _("product image")
    verbose_name_plural = _("product images")


class Stock(models.Model):
  product_inventory = models.OneToOneField(ProductInventory, on_delete=models.PROTECT, related_name="product_inventory")
  last_checked = models.DateTimeField(unique=False, null=True, blank=True, verbose_name=_("inventory stock check date"), help_text=_("format: Y-m-d H:M:S, null-true, blank-true"))
  units = models.IntegerField(default=0, unique=False, null=False, blank=False, verbose_name=_("units/qty of stock"), help_text=_("format: required, default-0"))
  units_sold = models.IntegerField(default=0, unique=False, null=False, blank=False, verbose_name=_("units sold to date"), help_text=_("format: required, default-0"))




class ProductAttributeValues(models.Model):
  attributevalues = models.ForeignKey(ProductAttributeValue, related_name="attributevaluess", on_delete=models.PROTECT)
  productinventory = models.ForeignKey(ProductInventory, related_name="productattributevaluess", on_delete=models.PROTECT)

  class Meta:
    unique_together = (("attributevalues", "productinventory"),)