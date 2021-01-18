from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Home(models.Model):
	owner = models.OneToOneField(User, on_delete=models.CASCADE)

	def __str__(self):
		return f"{ self.owner } 's home"


class Room(models.Model):
	ROOM_CHOICES = [
	    ("1", "living_room"),
	    ("2", "work_room"),
	    ("3", "bed_room"),
	    ("4", "kitchen")
	]
	home = models.ForeignKey(Home, on_delete=models.CASCADE, related_name='rooms')
	title = models.CharField(max_length=200, blank=True, choices=ROOM_CHOICES, default="1")

	def __str__(self):
		return f'HOME_ID: { self.home.owner } ; ROOM: { self.get_name }'

	@property
	def get_name(self):
		return self.get_title_display()
	

class Specs(models.Model):
	room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="specs", null=True)
	temperature = models.DecimalField(max_digits=5, decimal_places=2)
	humidity = models.DecimalField(max_digits=5, decimal_places=2)
	gas = models.PositiveIntegerField()
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ('-created', )

	def __str__(self):
		return f'Specs { self.id }'

	@property
	def status(self):
		if self.gas <= 500:
			return "Safe"
		else:
			return "Warning!"
	



