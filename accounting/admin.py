from django.contrib import admin

from accounting.models import TaxDefinition, Tax, Income, Expense


@admin.register(TaxDefinition)
class TaxDefinitionAdmin(admin.ModelAdmin):
    list_display = ('name', 'rate')


class TaxInline(admin.TabularInline):
    model = Tax


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('date', 'description', "ammount")
    inlines = [TaxInline]


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('date', 'description', "ammount")
    inlines = [TaxInline]

