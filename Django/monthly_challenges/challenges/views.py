from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404# type: ignore
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges={
    "jan": "F U 1",
    "feb": "F U 2",
    "mar": "F U 3",
    "apr": "F U 4",
    "may": "F U 5",
    "june": "F U 6",
    "july": "F U 7",
    "aug": "F U 8",
    "sept": "F U 9",
    "oct": "F U 10",
    "nov": None,
    "dec": "F U 12"
}

# Create your views here.

def months(request):
    list_items=""
    months=list(monthly_challenges.keys())
    
    return render(request,"challenges/index.html",{"month_list": months})
    
    #for month in months:
     #   month_path = reverse("month-challenge", args=[month])
    #    list_items+=f"<li><a href=\"{month_path}\">{month}</a></li>"
    
    #response_data=f"<ul>{list_items}</ul>"
    #return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):
    months=list(monthly_challenges.keys())
    if month>len(months):
        return HttpResponseNotFound("Invalid Month")
    redirect_month=months[month-1]
    redirect_path=reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text=monthly_challenges[month]
        return render(request,"challenges/challenge.html",{"month": month.capitalize(),"text": challenge_text})
        #response_data=f"<h1>{challenge_text}</h1>"
        #response_data=render_to_string("challenges/challenge.html")
        #return HttpResponse(response_data) 
    except:
        raise Http404()
        #responsedata= render_to_string("404.html")
        #return HttpResponseNotFound(responsedata)