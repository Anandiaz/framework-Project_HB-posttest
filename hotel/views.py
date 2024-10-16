from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib import messages
from .models import Hotel
from .forms import BookingForm, HotelForm
from datetime import date
from django.http import JsonResponse
from django.db.models import Q

# Create your views here.
def homepage(request):
    return render(request, "homepage/index.html")

# Verify the MEDIA_URL to all templates
def media_url_processor(request):
    return {
        "MEDIA_URL": settings.MEDIA_URL,
    }

# READ Hotel
def hotel_index(request):
    query = request.GET.get('q')
    hotel = Hotel.objects.all()
    if query:
        hotel = Hotel.objects.filter(
            Q(Name__icontains=query) |
            Q(Location__icontains=query) | 
            Q(ContactInfo__icontains=query) 
        )
    
    return render(request, 'crud/index.html', {'hotels': hotel, 'query': query})

# CREATE Hotel
def hotel_create(request):
    if request.method == 'POST':
        form = HotelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Hotel berhasil dibuat")
            return redirect('crud')
    else:
        form = HotelForm()
    return render(request, 'CRUD/create.html', {'form':form})   
        
# UPDATE Hotel
def hotel_update(request, hotel_id):
    hotel = get_object_or_404(Hotel, HotelID = hotel_id)
    if request.method == 'POST':
        form = HotelForm(request.POST, instance = hotel)
        if form.is_valid():
            form.save
            messages.success(request, "Hotel Berhasil Diubah")
            return redirect("crud")
    else:
        form = HotelForm(instance=hotel)
    return render (request, "CRUD/update.html", {'form':form, 'hotels': hotel})    

# DELETE Hotel
def hotel_delete(request, hotel_id):
    hotel = get_object_or_404(Hotel, HotelID=hotel_id)
    hotel.delete()
    messages.success(request, "Data Berhasil Dihapus")
    return JsonResponse({'success': True})
    

# Buat Booking Tapi blm jadi
def booking_index(request):
    query = request.GET.get('q')
    hotel = Hotel.objects.all()
    if query:
        hotel = Hotel.objects.filter(
            Q(Name__icontains=query) |
            Q(Location__icontains=query) | 
            Q(ContactInfo__icontains=query) 
        )
    
    return render(request, 'booking/index.html', {'hotels': hotel, 'query': query})

def booking_view(request, hotel_id):
    hotel = get_object_or_404(Hotel, HotelID=hotel_id)
    
    # Retrieve parameters from the URL
    start_date = request.GET.get('start_date', date.today().strftime('%Y-%m-%d'))
    end_date = request.GET.get('end_date', date.today().strftime('%Y-%m-%d'))
    room_count = request.GET.get('room_count', 1)  
    guest_count = request.GET.get('guest_count', 1)
    
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            return redirect('booking_confirmation')  
    else:
        form = BookingForm(initial={
            'start_date': start_date,
            'end_date': end_date,
            'room_count': room_count,
            'guest_count': guest_count,
        })

    return render(request, 'booking/booking_view.html', {
        'hotel': hotel,
        'form': form,
        'today': date.today(),
    })

def booking_confirmation(request):
    return render(request, 'booking/booking_confirmation.html', {})