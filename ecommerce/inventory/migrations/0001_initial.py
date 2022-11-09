# Generated by Django 4.1.3 on 2022-11-09 15:45

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Brand",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="format: required, max-255",
                        max_length=255,
                        unique=True,
                        verbose_name="brand name",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="format: required, max-100",
                        max_length=100,
                        verbose_name="category name",
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        help_text="format: required, letters, numbers, underscore, or hyphens",
                        max_length=150,
                        verbose_name="category safe url",
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("lft", models.PositiveIntegerField(editable=False)),
                ("rght", models.PositiveIntegerField(editable=False)),
                ("tree_id", models.PositiveIntegerField(db_index=True, editable=False)),
                ("level", models.PositiveIntegerField(editable=False)),
                (
                    "parent",
                    mptt.fields.TreeForeignKey(
                        blank=True,
                        help_text="format: not required",
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="children",
                        to="inventory.category",
                        verbose_name="parent of category",
                    ),
                ),
            ],
            options={
                "verbose_name": "product category",
                "verbose_name_plural": "product categories",
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "web_id",
                    models.CharField(
                        help_text="format: required, unique",
                        max_length=50,
                        unique=True,
                        verbose_name="product website ID",
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        help_text="format: required, letters, numbers, underscores of hyphens",
                        max_length=255,
                        verbose_name="product safe url",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="format: required, max-255",
                        max_length=255,
                        verbose_name="product name",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        help_text="format: required", verbose_name="product description"
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="format: true=product visibility",
                        verbose_name="product visibility",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="format: Y-m-d H:M:S",
                        verbose_name="data product created",
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="format: Y-m-d H:M:S",
                        verbose_name="data product last updated",
                    ),
                ),
                ("category", mptt.fields.TreeManyToManyField(to="inventory.category")),
            ],
        ),
        migrations.CreateModel(
            name="ProductType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="format: required, max-255",
                        max_length=255,
                        unique=True,
                        verbose_name="type of product",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProductInventory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "sku",
                    models.CharField(
                        help_text="format: required, unique, max-50",
                        max_length=50,
                        unique=True,
                        verbose_name="stock keeping unit",
                    ),
                ),
                (
                    "upc",
                    models.CharField(
                        help_text="format: required, unique, max-15",
                        max_length=15,
                        unique=True,
                        verbose_name="universal product code",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="format: true=product visibility",
                        verbose_name="product visibility",
                    ),
                ),
                (
                    "retail_price",
                    models.DecimalField(
                        decimal_places=2,
                        error_messages={
                            "name": {
                                "max_length": "the price must be between 0 and 999.99."
                            }
                        },
                        help_text="format: maximum price 999.99",
                        max_digits=5,
                        verbose_name="recommended retail price",
                    ),
                ),
                (
                    "store_price",
                    models.DecimalField(
                        decimal_places=2,
                        error_messages={
                            "name": {
                                "max_length": "the price must be between 0 and 999.99."
                            }
                        },
                        help_text="format: maximum price 999.99",
                        max_digits=5,
                        verbose_name="regular store price",
                    ),
                ),
                (
                    "sale_price",
                    models.DecimalField(
                        decimal_places=2,
                        error_messages={
                            "name": {
                                "max_length": "the price must be between 0 and 999.99."
                            }
                        },
                        help_text="format: maximum price 999.99",
                        max_digits=5,
                        verbose_name="sale price",
                    ),
                ),
                ("weight", models.FloatField(verbose_name="product weight")),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="format: Y-m-d H:M:S",
                        verbose_name="data sub-product created",
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="format: Y-m-d H:M:S",
                        verbose_name="data sub-product updated",
                    ),
                ),
                (
                    "brand",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="brand",
                        to="inventory.brand",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="product",
                        to="inventory.product",
                    ),
                ),
                (
                    "product_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="product_type",
                        to="inventory.producttype",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Media",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        default="images/default.png",
                        help_text="format: required, default-default.png",
                        upload_to="images/",
                        verbose_name="product image",
                    ),
                ),
                (
                    "alt_text",
                    models.CharField(
                        help_text="format: required, max-255",
                        max_length=255,
                        verbose_name="alternative text",
                    ),
                ),
                (
                    "is_feature",
                    models.BooleanField(
                        default=False,
                        help_text="format: default=false, true=default image",
                        verbose_name="product default image",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="format: Y-m-d H:M:S",
                        verbose_name="data sub-product created",
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="format: Y-m-d H:M:S",
                        verbose_name="data sub-product updated",
                    ),
                ),
                (
                    "product_inventory",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="media_product_inventory",
                        to="inventory.productinventory",
                    ),
                ),
            ],
            options={
                "verbose_name": "product image",
                "verbose_name_plural": "product images",
            },
        ),
    ]
