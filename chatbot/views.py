from django.http import JsonResponse
from django.shortcuts import render
import openai

openai_api_key='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'
openai.api_key=openai_api_key

def ask_openai(message):
    response=openai.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=message,
        max_tokens=150,
        stop=None,
        temperature=0.7,
    )
    print(response)
    answer=response.choice[0].text.strip()
    return answer

# Create your views here.
def chatbot(request):
    if request.method=='POST':
        message=request.POST.get('message')
        response= ask_openai(message)
        return JsonResponse({'message':message, 'response':response})
    return render(request, 'chatbot.html') #to show which file to render in the frontend