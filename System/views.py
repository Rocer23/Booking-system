from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from System.models import Room, Booking, Facility
from django.http import HttpResponse
from django.contrib.auth import login


# Create your views here.


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")
    else:
        form = UserCreationForm()

    return render(request, "booking/register.html", {'form': form})


def index(request):
    context = {
        "render_string": "Hello, World!"
    }
    return render(request, template_name='booking/index.html', context=context)


def room_list(request):
    rooms = Room.objects.all()
    context = {
        "rooms": rooms,
    }
    return render(request, template_name='booking/rooms_list.html', context=context)


def book_room(request):
    if request.method == "POST":
        room_number = request.POST.get("room-number")
        start_time = request.POST.get("start-time")
        end_time = request.POST.get("end-time")

        try:
            room = Room.objects.get(number=room_number)
        except ValueError:
            return HttpResponse(
                "Wrong room number!",
                status=400
            )
        except Room.DoesNotExist:
            return HttpResponse(
                "This room number doesn't exists",
                status=404
            )
        booking = Booking.objects.create(
            user=request.user,
            room=room,
            start_time=start_time,
            end_time=end_time
        )
        return redirect("booking-details", pk=booking.id)
    else:
        return render(request, template_name="booking/booking_form.html")


def booking_details(request, pk):
    try:
        booking = Booking.objects.get(id=pk)
        context = {
            "booking": booking
        }
        return render(request, template_name="booking/booking_details.html", context=context)
    except Booking.DoesNotExist:
        return HttpResponse(
            "This booking doesn't exists",
            status=404
        )

def booking_list(request):
    if request.user.is_authenticated:
        bookings = Booking.objects.filter(user=request.user)
        return render(
            request,
            template_name="booking/booking_list.html",
            context={"bookings": bookings}
        )
    else:
        return redirect("login")


def facilities_list(request):
    facilities = Facility.objects.all()
    return render(request, 'booking/facilities_list.html', {"facilities": facilities})

