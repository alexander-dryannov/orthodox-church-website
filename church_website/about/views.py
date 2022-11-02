from django.shortcuts import render


def clergy_page(request):
    return render(request, 'clergy.html')


def contacts_page(request):
    return render(request, 'contacts.html')


def donation_page(request):
    return render(request, 'donation.html')