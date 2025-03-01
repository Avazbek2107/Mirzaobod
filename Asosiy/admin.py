from django.contrib import admin
from .models import (
    Togaraklar,
    Tanlov,
    Tadbir,
    Konfirensiya,
    Rahbariyat,
    Oxirgi_ishlar, Budjet, Numbers, Hududiy_Rahbariyat, Korrupsiya_kurash, Contact,
)


@admin.register(Togaraklar)
class TogaraklarAdmin(admin.ModelAdmin):
    list_display = ['nomi', 'publish_time', 'active']
    list_filter = [
        'active',
        ('publish_time', admin.DateFieldListFilter),
    ]

    # data_hierarchy yil oy kun bo'yicha ajratish uchun ishlatiladi
    date_hierarchy = 'publish_time'
    search_fields = ['nomi']

    # ordering tartiblash uchun ishlatiladi birinchi active bo'yicha keyin boshlanish_sanasi
    ordering = ['active', 'publish_time']

    # quyidagi fieldlarni jadvalni o'zida to'g'irlash imkonini beradi editpagega kirmasdan
    list_editable = ['active']


@admin.register(Tadbir)
class TadbirAdmin(admin.ModelAdmin):
    list_display = ['nomi', 'boshlanish_sanasi', 'active']
    list_filter = [
        'active',
        ('boshlanish_sanasi', admin.DateFieldListFilter),
    ]

    # data_hierarchy yil oy kun bo'yicha ajratish uchun ishlatiladi
    date_hierarchy = 'boshlanish_sanasi'
    search_fields = ['nomi']

    # ordering tartiblash uchun ishlatiladi birinchi active bo'yicha keyin boshlanish_sanasi
    ordering = ['active', 'boshlanish_sanasi']

    # quyidagi fieldlarni jadvalni o'zida to'g'irlash imkonini beradi editpagega kirmasdan
    list_editable = ['active']


@admin.register(Tanlov)
class TanlovAdmin(admin.ModelAdmin):
    list_display = ['nomi', 'boshlanish_sanasi', 'active']
    list_filter = [
        'active',
        ('boshlanish_sanasi', admin.DateFieldListFilter),
    ]

    # data_hierarchy yil oy kun bo'yicha ajratish uchun ishlatiladi
    date_hierarchy = 'boshlanish_sanasi'
    search_fields = ['nomi']

    # ordering tartiblash uchun ishlatiladi birinchi active bo'yicha keyin boshlanish_sanasi
    ordering = ['active', 'boshlanish_sanasi']

    # quyidagi fieldlarni jadvalni o'zida to'g'irlash imkonini beradi editpagega kirmasdan
    list_editable = ['active']


@admin.register(Rahbariyat)
class RahbariyatAdmin(admin.ModelAdmin):
    list_display = ['name', 'last_name', 'fathers_name', 'publish_time']
    list_filter = [
        ('publish_time', admin.DateFieldListFilter),
    ]

    # slugni avtomatik to'ldirish keyinchalik
    # prepopulated_fields = {'slug': ('title',)}

    # data_hierarchy yil oy kun bo'yicha ajratish uchun ishlatiladi
    date_hierarchy = 'publish_time'
    search_fields = ['name', 'last_name', 'fathers_name']

    # ordering tartiblash uchun ishlatiladi birinchi active bo'yicha keyin boshlanish_sanasi
    ordering = ['publish_time']

    # tahrirlash oynasni ochadi berilgan fieldlarni ustiga borganda
    list_display_links = ['name', 'last_name', 'fathers_name']


@admin.register(Konfirensiya)
class KonfirensiyaAdmin(admin.ModelAdmin):
    list_display = ['nomi', 'boshlanish_sanasi', 'active']
    list_filter = [
        'active',
        ('boshlanish_sanasi', admin.DateFieldListFilter),
    ]

    # data_hierarchy yil oy kun bo'yicha ajratish uchun ishlatiladi
    date_hierarchy = 'boshlanish_sanasi'
    search_fields = ['nomi']

    # ordering tartiblash uchun ishlatiladi birinchi active bo'yicha keyin boshlanish_sanasi
    ordering = ['active', 'boshlanish_sanasi']

    # quyidagi fieldlarni jadvalni o'zida to'g'irlash imkonini beradi editpagega kirmasdan
    list_editable = ['active']


@admin.register(Oxirgi_ishlar)
class Oxirgi_ishlarAdmin(admin.ModelAdmin):
    list_display = ['nomi', 'publish_time', 'active']
    list_filter = [
        'active',
        ('publish_time', admin.DateFieldListFilter),
    ]

    # data_hierarchy yil oy kun bo'yicha ajratish uchun ishlatiladi
    date_hierarchy = 'publish_time'
    search_fields = ['nomi']

    # ordering tartiblash uchun ishlatiladi birinchi active bo'yicha keyin boshlanish_sanasi
    ordering = ['active', 'publish_time']

    # quyidagi fieldlarni jadvalni o'zida to'g'irlash imkonini beradi editpagega kirmasdan
    list_editable = ['active']


@admin.register(Budjet)
class BudjetAdmin(admin.ModelAdmin):
    list_display = ['nomi', 'publish_time', 'active', 'narxi', 'date']
    list_filter = [
        'active',
        ('publish_time', admin.DateFieldListFilter),
    ]

    # data_hierarchy yil oy kun bo'yicha ajratish uchun ishlatiladi
    date_hierarchy = 'publish_time'
    search_fields = ['nomi']

    # ordering tartiblash uchun ishlatiladi birinchi active bo'yicha keyin boshlanish_sanasi
    ordering = ['active', 'publish_time']

    # quyidagi fieldlarni jadvalni o'zida to'g'irlash imkonini beradi editpagega kirmasdan
    list_editable = ['active']


admin.site.register(Numbers)


@admin.register(Hududiy_Rahbariyat)
class Hududiy_RahbariyatAdmin(admin.ModelAdmin):
    list_display = ['name', 'last_name', 'fathers_name', 'publish_time']
    list_filter = [
        ('publish_time', admin.DateFieldListFilter),
    ]

    # slugni avtomatik to'ldirish keyinchalik
    # prepopulated_fields = {'slug': ('title',)}

    # data_hierarchy yil oy kun bo'yicha ajratish uchun ishlatiladi
    date_hierarchy = 'publish_time'
    search_fields = ['name', 'last_name', 'fathers_name']

    # ordering tartiblash uchun ishlatiladi birinchi active bo'yicha keyin boshlanish_sanasi
    ordering = ['publish_time']

    # tahrirlash oynasni ochadi berilgan fieldlarni ustiga borganda
    list_display_links = ['name', 'last_name', 'fathers_name']


@admin.register(Korrupsiya_kurash)
class Korrupsiya_kurashAdmin(admin.ModelAdmin):
    list_display = ['nomi', 'publish_time', 'active']
    list_filter = [
        'active',
        ('publish_time', admin.DateFieldListFilter),
    ]

    # data_hierarchy yil oy kun bo'yicha ajratish uchun ishlatiladi
    date_hierarchy = 'publish_time'
    search_fields = ['nomi']

    # ordering tartiblash uchun ishlatiladi birinchi active bo'yicha keyin boshlanish_sanasi
    ordering = ['active', 'publish_time']

    # quyidagi fieldlarni jadvalni o'zida to'g'irlash imkonini beradi editpagega kirmasdan
    list_editable = ['active']

admin.site.register(Contact)




