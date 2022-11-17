# Generated by Django 4.1 on 2022-11-17 01:58

import colorfield.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import equipe.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, unique=True)),
                ('descricao', models.CharField(blank=True, max_length=150, null=True, verbose_name='Descrição')),
                ('salario', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Salário')),
                ('administrador', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Setor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, unique=True)),
                ('descricao', models.CharField(blank=True, max_length=150, null=True, verbose_name='Descrição')),
                ('cor', colorfield.fields.ColorField(default='#808080', image_field=None, max_length=18, samples=None)),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primeiro_nome', models.CharField(max_length=20, verbose_name='Primeiro Nome')),
                ('segundo_nome', models.CharField(max_length=80, verbose_name='Sobrenome')),
                ('cpf', models.CharField(max_length=14, unique=True, validators=[equipe.models.Funcionario.validate_cpf])),
                ('ctps', models.CharField(max_length=14, unique=True, validators=[equipe.models.Funcionario.validate_ctps])),
                ('dataNascimento', models.DateField(default='01/01/2000', verbose_name='Data de Nascimento')),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('tel', models.CharField(help_text='Com DDD.', max_length=15, verbose_name='Telefone')),
                ('rua', models.CharField(max_length=30, verbose_name='Rua ou Avenida')),
                ('numero', models.IntegerField(verbose_name='Número')),
                ('bairro', models.CharField(max_length=15, verbose_name='Bairro ou Jardim')),
                ('cidade', models.CharField(max_length=30)),
                ('bonusMensal', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Bônus Salarial Mensal')),
                ('dataContratacao', models.DateField(default=django.utils.timezone.now, verbose_name='Data de Contratação')),
                ('observacao', models.CharField(blank=True, max_length=255, null=True, verbose_name='Observação')),
                ('dataDemicao', models.DateField(blank=True, null=True, verbose_name='Data Demissional:')),
                ('demitido', models.BooleanField(default=False, verbose_name='Demitido:')),
                ('salTotal', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True, verbose_name='Salário Total')),
                ('motivoDemicao', models.CharField(blank=True, max_length=100, null=True, verbose_name='Motivo da Demissão:')),
                ('administrador', models.BooleanField(default=False)),
                ('contaFuncionario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('funcao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='equipe.cargo', verbose_name='Função')),
            ],
        ),
        migrations.AddField(
            model_name='cargo',
            name='setor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='equipe.setor', verbose_name='Setor'),
        ),
    ]
