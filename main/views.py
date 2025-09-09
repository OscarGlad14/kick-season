from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'NamaToko' : 'Kick Season',
        'Nama': 'Oscar Glad Winfi Simanullang',
        'Kelas': 'PBP E'
    }

    return render(request, "main.html", context)