from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    product_relationship = models.OneToOneField(
        'Product_relationship', blank=True, null=True, related_name='+')


class Product_relationship(models.Model):
    relation_type = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    related_product = models.ForeignKey(
        'Product', blank=True, null=True, related_name='+')
    relating_product = models.ForeignKey(
        'Product', blank=True, null=True, related_name='+')


class Product_version(models.Model):
    description = models.TextField(blank=True, null=True)
    product = models.OneToOneField('Product', blank=True, null=True)
    relationship = models.ForeignKey(
        'Product_version_relationship', blank=True, null=True)


class Product_version_relationship(models.Model):
    description = models.TextField(blank=True, null=True)
    related_version = models.ForeignKey(
        'Product_version', blank=True, null=True, related_name='+')
    relating_version = models.ForeignKey(
        'Product_version', blank=True, null=True, related_name='+')


class Product_category(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    assigment = models.OneToOneField(
        'Product_category_assignment', blank=True, null=True, related_name='category')


class Product_category_assignment(models.Model):
    products = models.ManyToManyField('Product', related_name="categories")


class Product_category_hierarchy(models.Model):
    sub_category = models.ForeignKey('Product_category', blank=True,
        null=True, related_name='+')
    super_category = models.ForeignKey('Product_category', blank=True,
        null=True, related_name='+')

class Product_view_definition(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    additionnal_characterization = models.TextField(blank=True, null=True)
    relating_view  = models.ForeignKey('self', blank=True, null=True,
        related_name='related_view')
    contexts = models.ManyToManyField('View_definition_context')


class View_definition_context(models.Model):
    application_domain = models.CharField(max_length=100)
    life_cycle_stage = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)


class Product_property_assignment(models.Model):
    pass


class View_definition_relationship(models.Model):
    relation_type = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)


class View_definition_usage(View_definition_relationship):
    pass


class Assembly_component_relationship(View_definition_usage):
    location_indicator = models.TextField(blank=True, null=True)
    quantity = models.ForeignKey('Value_with_unit', blank=True, null=True)
    substitute = models.ForeignKey('self', blank=True, null=True)

class Next_assembly_usage(Assembly_component_relationship):
    sub_assembly_relationship = models.ForeignKey(
        'Component_upper_level_identification', blank=True, null=True)

class Component_upper_level_identification(Assembly_component_relationship):
    pass


class Promissory_usage(Assembly_component_relationship):
    pass


class Value_with_unit(models.Model):
    unit = models.ForeignKey('Unit')
    value_component = models.ForeignKey('Measure_value')

class Unit(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    si_unit = models.CharField(max_length=100, blank=True, null=True)


class Measure_value(models.Model):
    pass


class any_number_value(Measure_value):
    any_number_value = models.IntegerField()
