from django.contrib import admin
from django.contrib.auth.hashers import make_password
from .models import Booking, User, Room, Hotel  # Adjust the import based on your project structure

class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'room', 'check_in_date', 'check_out_date', 'total_price', 'booking_status')

    def save_model(self, request, obj, form, change):
        # Save the booking first
        super().save_model(request, obj, form, change)

        # Check if the user already exists based on their email
        user_email = obj.user.email
        user, created = User.objects.get_or_create(email=user_email, defaults={
            'username': obj.user.username,
            'password': make_password('default_password'),  # Hashing password
            'phone_number': obj.user.phone_number,
        })

        if not created:
            # If the user already exists, update their information if necessary
            user.username = obj.user.username
            user.phone_number = obj.user.phone_number
            user.save()

# Register the Booking model with the custom BookingAdmin
admin.site.register(Booking, BookingAdmin)
# Register other models as needed
admin.site.register(User)
admin.site.register(Room)
admin.site.register(Hotel)