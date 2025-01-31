from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages

from .forms import DestinationForm, DestinationSearchForm
from accounts.models import Destination


# Handles the search functionality and pagination for the list of destinations
def destination_list(request):
    form = DestinationSearchForm(request.GET or None)
    query = request.GET.get('query', '')
    if query:
        destinations_list = Destination.objects.filter(
            Q(name__icontains=query) |
            Q(country__icontains=query) |
            Q(description__icontains=query) |
            Q(best_time_to_visit__icontains=query) |
            Q(budget_type__icontains=query)
        )
    else:
        destinations_list = Destination.objects.all()

    paginator = Paginator(destinations_list, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'destination_list.html', {'page_obj': page_obj})


# Handles the creation of a new destination by the logged-in user
@login_required
def destination_create(request):
    if request.method == 'POST':
        form = DestinationForm(request.POST, request.FILES)
        if form.is_valid():
            destination = form.save(commit=False)
            destination.user = request.user
            destination.save()

            if form.cleaned_data.get('is_favorite'):
                destination.is_favorite = True
                destination.favorites.add(request.user)
                destination.save()

            messages.success(request, "Destination added successfully")
            return redirect('destination_list')
    else:
        form = DestinationForm()

    return render(request, 'destination_form.html', {
        'form': form,
        'is_update': False
    })


# Displays the details of a single destination
def destination_detail(request, id):
    destination = get_object_or_404(Destination, id=id)
    return render(request, 'destination_detail.html', {
        'destination': destination
    })


# Displays the list of destinations created by the logged-in user
@login_required
def mydestination(request):
    destinations = Destination.objects.filter(user=request.user)
    return render(request, 'mydestination.html', {
        'destinations': destinations,
        'username': request.user.username
    })


# Allows the user to update the details of an existing destination
def destination_update(request, destination_id):
    destination = get_object_or_404(Destination, id=destination_id)
    if request.method == 'POST':
        form = DestinationForm(
            request.POST, request.FILES, instance=destination)
        if form.is_valid():
            form.save()
            messages.success(request, 'Destination updated')
            return redirect('destination_detail', id=destination_id)
    else:
        form = DestinationForm(instance=destination)

    return render(request, 'destination_form.html', {
        'form': form,
        'is_update': True,
        'destination': destination
    })


# Deletes a destination after user confirmation
def destination_delete(request, destination_id):
    destination = get_object_or_404(Destination, id=destination_id)
    if request.method == 'POST':
        destination.delete()
        return redirect('mydestination')

    return render(request, 'destination_delete.html', {
        'destination': destination
    })


# Adds or removes a destination from the logged-in user's favorites
@login_required
def favorite_destination(request, destination_id):
    destination = get_object_or_404(Destination, id=destination_id)
    if request.user in destination.favorites.all():
        destination.favorites.remove(request.user)
        messages.success(request, "Removed from favorites")
    else:
        destination.favorites.add(request.user)
        messages.success(request, "Added to favorites")

    return redirect('destination_detail', id=destination.id)


# Displays the list of favorite destinations for the logged-in user
@login_required
def my_favorites(request):
    favorite_destinations = Destination.objects.filter(favorites=request.user)
    paginator = Paginator(favorite_destinations, 6)  # Show 6 destinations
    page_number = request.GET.get('page')  # Get the page number
    page_obj = paginator.get_page(page_number)  # Get the paginated items

    return render(request, 'my_favorites.html', {
        'favorite_destinations': page_obj
    })


# Allows the user to like or unlike a destination
def likes_destination(request, destination_id):
    destination = get_object_or_404(Destination, id=destination_id)
    if request.user in destination.likes.all():
        destination.likes.remove(request.user)
    else:
        destination.likes.add(request.user)

    return redirect('destination_detail', id=destination.id)
