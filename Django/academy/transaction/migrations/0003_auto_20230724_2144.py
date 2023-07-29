# Generated by Django 3.2 on 2023-07-24 21:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0002_userbalance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transaction_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Charge'), (2, 'Purchase'), (4, 'Transfer sent'), (3, 'Transfer Received')], default=1),
        ),
        migrations.CreateModel(
            name='TransferTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiver_transaction', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='receiver', to='transaction.transaction')),
                ('sender_transaction', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='sender', to='transaction.transaction')),
            ],
        ),
    ]