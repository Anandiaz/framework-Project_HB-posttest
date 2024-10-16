from django import forms
from .models import Hotel

class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = '__all__'


# Buat Booking Hotel tapi blm bisa
class BookingForm(forms.Form):
    hotel_id = forms.IntegerField(widget=forms.HiddenInput())  # Hidden field for hotel ID
    start_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        label='Start Date'
    )
    end_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        label='End Date'
    )
    room_count = forms.IntegerField(
        min_value=1,
        initial=1,
        label='Room',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    guest_count = forms.IntegerField(
        min_value=1,
        initial=1,
        label='Guest',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    def __init__(self, *args, **kwargs):
        self.current_user = kwargs.pop('current_user', None)  # Get current user if provided
        super().__init__(*args, **kwargs)

    def save(self):
        # Here you can implement logic to save the booking if needed
        # For example, create a Booking instance using self.cleaned_data
        pass