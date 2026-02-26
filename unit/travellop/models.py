from django.db import models

class Appointment(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.appointment_date} {self.appointment_time}"

class unit():
    id: int
    name: str
    img: str
    description: str
    price: int
    
