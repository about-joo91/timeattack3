from django.shortcuts import render
from django.http import HttpResponse
from .models import User
import hashlib
import json
# Create your views here.


def sign_up(request):
    request_body = json.loads(request.body)
    email = request_body.get('email', '')
    password = request_body.get('password', '')
    
    if '@' not in email:
        print(email)
        return HttpResponse('이메일이 아닙니다')
    elif len(password) < 8:
        return HttpResponse('비밀번호 길이 에러')
    else:
        password = password.encode()
        hashed_password = hashlib.sha256(password).hexdigest() 
        new_user = User(user_id=email, password=hashed_password)
        return HttpResponse('회원가입 완료')