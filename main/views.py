from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306210286',
        'name': 'Yeshua Marco Gracia Manurung',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)