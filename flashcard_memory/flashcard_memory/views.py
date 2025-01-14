from django.shortcuts import render, redirect
from flashcard.models import Deck

def landing_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        if username:
            return redirect('dashboard', username=username)
    return render(request, 'landing_page.html')

def dashboard(request, username):
    user_decks = Deck.objects.filter(user__username=username)
    return render(request, 'dashboard.html', {'username': username, 'user_decks': user_decks})