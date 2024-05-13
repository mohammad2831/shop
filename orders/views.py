from django.shortcuts import render
from django.views import View

class CardsView(View):
    def get(self, request):
        return render(request,'orders/cards.html')
