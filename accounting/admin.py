from django.contrib import admin

from accounting.models import Tax, Income, Expense, RecordItem


@admin.register(Tax)
class TaxAdmin(admin.ModelAdmin):
    list_display = ('name', 'rate')


class RecordItemInline(admin.TabularInline):
    model = RecordItem


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('date',)
    inlines = [RecordItemInline]


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('date',)
    inlines = [RecordItemInline]

