from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import promptconstructor, openai


# Create your views here.

def index(request):
    return render(request, "app/index.html")


@csrf_exempt
def prompt(request):
    user_message = request.POST.get('prompt', None)
    
    prompt = promptconstructor.buildPrompt(user_message)
    
    response = {"response": openai.chat3turbo(prompt)}
    
    print(response)
    return(JsonResponse(response))