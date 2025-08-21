from django.http import JsonResponse


def home_page(request):
    print('home page request')

    friends = [
        'Ahmad',
        'Umeer',
        'Shazad',
    ]

    return JsonResponse(friends, safe=False)
