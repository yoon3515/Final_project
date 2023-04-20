from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse
from django.shortcuts import render, redirect
from accounts.forms import UserForm
from pymongo import MongoClient

# Create your views here.

def signup(request):
  if request.method == "POST":
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password1']
        
    try:
      # MongoDB 연결
      client = MongoClient('mongodb://localhost:27017/')
      db = client['mul_db']
      users = db['users']

      # user 중복 확인
      if users.find_one({'username': username}):
        return HttpResponse('User already exists')

      # user 데이터 저장
      user = {
        'username': username,
        'email': email,
        'password': password
      }
      users.insert_one(user)

      return redirect('login')
    except Exception as e:
      # Handle the exception here
      print(f"DB 연결에 실패했습니다: {e}")
      return HttpResponse('Error connecting to MongoDB')
  
  form = UserForm(request.POST)
  if not form.is_valid():
    return render(request, 'accounts/signup.html', {'form': form})


def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    
    # Connect to MongoDB with authentication
    client = MongoClient('mongodb://localhost:27017/')
    db = client['mul_db']
    users = db['users']

    # Check if the user exists in MongoDB
    user = users.find_one({'username': username})
    if not user:
      return HttpResponse('User does not exist')

    # Check if the password matches the hashed password in MongoDB
    if not check_password(password, user['password']):
      return HttpResponse('Invalid password')
        
    # User authenticated, log them in and redirect to home page
    user_id = str(user['_id'])
    request.session['user_id'] = user_id
    return redirect('home')

  return render(request, 'login.html')
