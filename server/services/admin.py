from django.contrib import admin

from .models import Home, Room, Specs


class RoomInline(admin.StackedInline):
	model = Room
	extra = 0


class HomeAdmin(admin.ModelAdmin):
	list_display = ['id', 'owner']
	inlines = [RoomInline]

admin.site.register(Home, HomeAdmin)


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
	list_display = ['title', 'home']


@admin.register(Specs)
class SpecsAdmin(admin.ModelAdmin):
	list_display = ['room', 'temperature', 'humidity', 'gas', 'created']