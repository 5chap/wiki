from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import random, markdown2
from django import forms
from . import util

# Define a form class to take new entries
class NewEntryForm(forms.Form):
    title = forms.CharField(max_length=80)
    values = forms.CharField(widget=forms.Textarea)



# Display all entries on the home page
def index(request):
    if util.get_entry(request.GET.get("q")) is not None:
        return HttpResponseRedirect("/" + request.GET.get("q"))
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

# Display a single entry title and content on title page template
def contents(request, TITLE):
    content = markdown2.markdown(util.get_entry(TITLE))
    return render(request, "encyclopedia/title.html", {
        "Contents": content, "TITLE": TITLE 
    })

# Display a randomly selected title on a new template
def new_page(request):
    allEntries = util.list_entries()
    randomEntry = random.choice(allEntries)
    return render(request, "encyclopedia/new_page.html", {
        "randomEntry": randomEntry
    })

# Create a new entry 
def newEntry(request):
    if request.method == "POST":
        entry=NewEntryForm(request.POST)
        if entry.is_valid():
            title = entry.cleaned_data['title']
            values = entry.cleaned_data['values']
            if title not in util.entries():
                util.save_entry(title, values)
                return render(request, "encyclopedia/index.html", {
                    "entries": util.list_entries()
                    })
            else:
                return HttpResponse("Entry already exist!")
                
        else:
            return render(request, "encyclopedia/newEntry.html", {
                    "entry":entry
            })
    else:
         return render(request, "encyclopedia/newEntry.html", {
                    "entry":NewEntryForm() 
            })


    

