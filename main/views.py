from django.shortcuts import render

# Create your views here.

def index(request):
  if request.POST:
    context = {
      'name': request.POST['name'],
      'email': request.POST['email'],
    }
    return render(request, 'thanks.html', context)
  context = {
    'results': [
      {'name': 'Fatima Lopez', 'email': 'f.lopez@email.com', 'status': 'Submitted'},
      {'name': 'Gary Johnston', 'email': 'g.johnston@email.com', 'status': 'Submitted'},
      {'name': 'Rodriguez Sam Neiol', 'email': 'rodriguez.sam@gmail.com', 'status': 'Submitted'},
      {'name': 'Mari Gotze', 'email': 'mario.gotze23@gmail.com', 'status': 'Submitted'},
      {'name': 'Omar Yussuf', 'email': 'omar.ysuf12@gmail.com', 'status': 'Submitted'}
    ]
  }
  return render(request, 'index.html', context)
