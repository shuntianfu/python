from django.shortcuts import render

# Create your views here.


def index(request):
    meetups = [
        {'title': 'A First Meetups', 'location': 'New York', 'slug': 'a-first-meetup'},
        {'title': 'A Second Meetups', 'location': 'Paris', 'slug': 'a-second-meetup'}
    ]
    return render(request, 'meetups/index.html', {
        'show_meetups': True,
        'meetups': meetups
    })


def meetup_details(request, meetup_slug):
    selected_meetup = {
        'title': 'A First meetup',
        'description': 'This is the first meetup!'
    }
    return render(request, 'meetups/meetup-details.html', {
        'meetup_title': selected_meetup['title'],
        'meetup_description': selected_meetup['description']
    })
