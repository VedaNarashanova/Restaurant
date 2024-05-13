from django.contrib import admin
from .models import Restaurant, Dish, DishRestaurant, Employee, BusinessHours
# Register your models here.


# class BusinessHoursInlineAdmin(admin.TabularInline):
#     model = BusinessHours
#     extra = 1
#
# class RestaurantAdmin(admin.ModelAdmin):
#     list_display = ('name', "email", "phone",) #za tabelarno prikazhuvanje na mail email phone
#     list_filter = ('capacity','name') #spored sto sakame da filtrirame
#
#     fieldsets = [# lista od torki, sekoja torka 2 elementi, prv element-ime na sekcija, vtor element-recnik, vo recnikot-klucot e bilds a vrednosta e lista od elementi koi sakame da bidat del od taa sekcija
#         (None, {'fields': ['name', 'address', 'capacity']}),
#         ("Contact", {'fields': ['email', 'phone', ]})
#     ]
#
#     inlines = [BusinessHoursInlineAdmin,]
#
#     def has_delete_permission(self, request, obj=None): #da se onevozmozhi mozhnosta za brisenje useri
#         if request.user.is_superuser:
#             return True
#         return False
#
#
#
# class EmployeeAdmin(admin.ModelAdmin):
#     exclude=("user",) #da ne se pokazhuva poleto user
#
#     def has_change_permission(self, request, obj=None):
#         if obj and obj.user == request.user:  # toj user go napravil i smee da si go brishe (dali userot na objektot == so tekovno najaveniot user)
#             return True
#         return False
#
#     def save_model(self,request,obj,form,change):#se povikuva od admin panelot koga ke se klikne save i se zacuvuva toj objekt vo baza, nie go presekuvame toj proces go vmetnuvame tekovno najaveniot korisnik i go pushtame
#         obj.user=request.user #userot na objektot sto momentalno se zacuvuva
#         return super(EmployeeAdmin,self).save_model(request,obj,form,change)
#
#
#
#
# class DishAdmin(admin.ModelAdmin):
#     list_display = ('name',)
#
#     def has_add_permission(self, request,obj=None): #onevozmozhuvanje dodavanje na sadovi
#         if request.user.is_superuser:
#             return True
#         return False
#
#
# admin.site.register(Restaurant, RestaurantAdmin)
# admin.site.register(Dish)
# admin.site.register(DishRestaurant)
# admin.site.register(Employee,EmployeeAdmin)
# # admin.site.register(BusinessHours)


admin.site.register(Restaurant)
admin.site.register(Dish)
admin.site.register(DishRestaurant)
admin.site.register(Employee)
admin.site.register(BusinessHours)