from django.contrib import admin
from transaction.models import Transaction, UserBalance
# Register your models here.


class TransactionAdmin(admin.ModelAdmin):
    list_display = ['user', 'transaction_type', 'amount', 'created_time']
    search_fields = ['user__username', 'transaction_type', 'created_time']
    list_filter = ['transaction_type']


class UserBalanceAdmin(admin.ModelAdmin):
    list_display = ['user', 'balance', 'created_time']
    search_fields = ['user__username']


admin.site.register(Transaction, TransactionAdmin)
admin.site.register(UserBalance, UserBalanceAdmin)
