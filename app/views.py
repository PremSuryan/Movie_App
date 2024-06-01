from django.shortcuts import render
from .models import insert_movie,comments
from django.http import HttpResponse
from .forms import insert_form,comment_movie
# Import necessary modules and models
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import logout
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication



@api_view(['POST'])
def login_page(request):
    # Check if the HTTP request method is POST (form submission)
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if a user with the provided username exists
        if not User.objects.filter(username=username).exists():
            # Display an error message if the username does not exist
            messages.error(request, 'Invalid Username')
            return Response({'error': 'Invalid Username'}, status=400)

        # Authenticate the user with the provided username and password
        user = authenticate(username=username, password=password)

        if user is None:
            # Display an error message if authentication fails (invalid password)
            messages.error(request, "Invalid Password")
            return Response({'error': 'Invalid Password'}, status=400)
        else:
            # Log in the user
            login(request)
            # Create or retrieve the token for the authenticated user
            token, created = Token.objects.get_or_create(user=user)
            # Return token information as part of the response
            return Response({
                'token': token.key,
                'user_id': user.pk,
                'username': user.username,
                'last_name': user.last_name,
                'first_name': user.first_name,
            }, status=200)

    # Render the login page template (GET request)
    return render(request, 'login.html')

# Define a view function for the registration page
def register_page(request):
	# Check if the HTTP request method is POST (form submission)
	if request.method == 'POST':
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		username = request.POST.get('username')
		password = request.POST.get('password')
		
		# Check if a user with the provided username already exists
		user = User.objects.filter(username=username)
		
		if user.exists():
			# Display an information message if the username is taken
			messages.info(request, "Username already taken!")
			return redirect('/register/')
		
		# Create a new User object with the provided information
		user = User.objects.create_user(
			first_name=first_name,
			last_name=last_name,
			username=username
		)
		
		# Set the user's password and save the user object
		user.set_password(password)
		user.save()
		
		# Display an information message indicating successful account creation
		messages.info(request, "Account created Successfully!")
		return redirect('login_page')
	
	# Render the registration page template (GET request)
	return render(request, 'register.html')

# Create your views here.
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def logout_view(request):
    try:
        request.user.auth_token.delete()
        logout(request)
        return Response(status=status.HTTP_200_OK)
    except AttributeError:
        return Response(status=status.HTTP_400_BAD_REQUEST)

# Define a view function for the home page


def login(request):
    if request.method =='GET':
        return render(request,'navbar.html')
    

def insert(request):

    form = insert_form()
    if request.method == 'POST' and request._files:
        form = insert_form(request.POST,request._files)
        if form.is_valid():
            form.save()
        return HttpResponse('Movie Inserted Into the Database')
    return render(request,'insertdata.html',{'form':form})


def view(request):
    form = insert_movie.objects.all()
    return render(request,'display.html',{'data':form})


def updatedata(request,id):
    form = insert_movie.objects.get(id=id)
    print('form:',form)

    data = insert_form(instance=form)
    print(f'data{data}')
    if request.method == 'POST' and request._files :
        data = insert_form(request.POST,request._files,instance=data)
        if data.is_valid():
            data.save()
        return HttpResponse('Data Updated sucessfully')
    return render(request,'insertdata.html',{'form':data})

def deletemovie(request,id):
    return render(request,'delete.html',{'id':insert_movie.objects.get(id=id).delete()})

def user_comments(request,id):
    data = insert_movie.objects.get(id=id)
    form1 = comment_movie(initial={'review':id})
    if request.method == 'POST':
        form1 = comment_movie(request.POST)
        if form1.is_valid():
            form1.save()
        return HttpResponse('comment posted')
    return render(request,'details.html',{'data':data,'form':form1})

def comment_view(request,id):
    data = comments.objects.get(id=id)
    
    return render(request,'usercommentview.html',{'data':data})

# class CustomObtainAuthToken(ObtainAuthToken):
#     def post(self, request, *args, **kwargs):
#         username = request.data.get('username')
#         password = request.data.get('password')
#         user = authenticate(username=username, password=password)
#         if user:
#             token, created = Token.objects.get_or_create(user=user)
#             return Response({'token': token.key, 'user_id': user.id})
#         else:
#             return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)


# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])




# class CustomAuthToken(ObtainAuthToken):
#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data, context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({
#             'token': token.key,
#             'user_id': user.pk,
#             'username': user.username,
#             'last_name': user.last_name,
#             'first_name': user.first_name,
#             # 'email': user.email
#         })
    