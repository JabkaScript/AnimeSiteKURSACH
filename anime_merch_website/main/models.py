from django.db import models


class Status(models.Model):
    status_id = models.AutoField(primary_key=True, blank=True, null=False)
    status_name = models.CharField(blank=True, null=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'status'


class Categories(models.Model):
    cat_id = models.AutoField(primary_key=True, blank=True, null=False)
    name = models.CharField(blank=True, null=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'categories'


class Clients(models.Model):
    client_id = models.AutoField(primary_key=True, blank=True, null=False)
    e_mail = models.CharField(blank=True, null=True, max_length=50)
    password = models.CharField(blank=True, null=True, max_length=50)
    surname = models.CharField(blank=True, null=True, max_length=50)
    first_name = models.CharField(blank=True, null=True, max_length=50)
    second_name = models.CharField(blank=True, null=True, max_length=50)
    telephon_number = models.CharField(blank=True, null=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'clients'


class Images(models.Model):
    kit_id = models.AutoField(primary_key=True, blank=True, null=False)
    preview = models.CharField(blank=True, null=True, max_length=500)
    desc1 = models.CharField(blank=True, null=True, max_length=500)
    desc2 = models.CharField(blank=True, null=True, max_length=500)
    desc3 = models.CharField(blank=True, null=True, max_length=500)

    class Meta:
        managed = False
        db_table = 'images'


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True, blank=True, null=False)
    status = models.ForeignKey(Status, models.DO_NOTHING, blank=True, null=True)
    client = models.ForeignKey(Clients, models.DO_NOTHING, blank=True, null=True)
    address = models.CharField(blank=True, null=True, max_length=250)
    comment = models.CharField(blank=True, null=True, max_length=250)

    class Meta:
        managed = False
        db_table = 'orders'


class Ordersproducts(models.Model):
    order = models.ForeignKey(Orders, models.DO_NOTHING, blank=True, null=False)
    product = models.ForeignKey('Products', models.DO_NOTHING, blank=True, null=False)
    count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ordersproducts'


class Products(models.Model):
    product_id = models.AutoField(primary_key=True, blank=True, null=False)
    cat = models.ForeignKey(Categories, models.DO_NOTHING, blank=True, null=True)
    product_name = models.CharField(blank=True, null=True, max_length=50)
    mass = models.TextField(blank=True, null=True, max_length=50)  # This field type is a guess.
    material = models.CharField(blank=True, null=True, max_length=50)
    size = models.CharField(blank=True, null=True, max_length=50)
    add_inf = models.CharField(blank=True, null=True, max_length=50)
    cost = models.IntegerField(blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    images = models.ForeignKey(Images, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products'

    def name(self):
        return str(self.product_name)


class Productstitles(models.Model):
    product = models.ForeignKey(Products, models.DO_NOTHING, blank=True, null=True)
    title = models.ForeignKey('Titles', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'productstitles'


class Titles(models.Model):
    title_id = models.AutoField(primary_key=True, blank=True, null=False)
    name = models.CharField(blank=True, null=True, max_length=50)
    author = models.CharField(blank=True, null=True, max_length=50)
    universe = models.CharField(blank=True, null=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'titles'
