from cgitb import text
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def counter(request):
    text = request.GET['text']
    amount_of_words = len(text.split())
    #gets text from index which has called it and splits the text by spaces, the assinging a variable with the len of the list of words.
    return render(request, 'counter.html', {'amount':amount_of_words})
    #