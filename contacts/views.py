from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import ContactForm

# Create your views here.

@login_required
def index(request):
    contacts = request.user.contacts.all().order_by("created_at")
    context = {
        "contacts":contacts,
        'form':ContactForm()
        }
    return render(request, 'contacts.html', context)

@login_required
def search_contacts(request):

    import time

    time.sleep(1)
    query = request.GET.get('search','')

    # use the query to filter contacts by name or email

    contacts = request.user.contacts.filter(
        Q(name__icontains=query) | Q(email__icontains=query)
    )

    return render(
        request,
        'partials/contacts-list.html',
        {'contacts':contacts}
        )

