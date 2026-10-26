from django.contrib import admin
from .models import Client, Product, Check
from import_export import admin as ie_admin

@admin.action()
def product_soni(modeladmin, request, queryset):
    queryset.update(quantity=0)
@admin.action(description="ismini qosim qilish")
def client_ism(modeladmin, request, queryset):
    queryset.update(first_name="Qosimjon")
    queryset.update(username="00000000")
@admin.action(description="ismini jasur qilish")
def client_ism2(modeladmin, request, queryset):
    queryset.update(first_name="Jasurjon")
    queryset.update(username="1111111111")


@admin.register(Client)
class ClientAdmin(ie_admin.ImportExportActionModelAdmin):
    list_display = ('username', 'first_name')
    actions = (client_ism, client_ism2)


@admin.register(Product)
class ProductAdmin(ie_admin.ImportExportActionModelAdmin):
    list_display = ('quality', 'name', 'price')
    actions = (product_soni,)


@admin.register(Check)
class CheckAdmin(ie_admin.ImportExportActionModelAdmin):
    list_display = ('client', 'product')