import smtplib
from _sha1 import sha1
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.http import HttpResponse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User as DjangoUser
from .models import *
from .forms import *
from user_agents import parse
from random import randint


def rend(request, template_name, context=None):
    if context is None:
        context = {}
    if parse(request.META.get("HTTP_USER_AGENT")).is_mobile:
        context['is_mobile'] = True
    else:
        context['is_mobile'] = False
    return render(request, template_name, context)


def error(request, message):
    return rend(request, 'store/error.html', {'error': message})


def home(request):
    print(request.user.__str__())
    return rend(request, 'store/home.html')


def loggin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form['username'].value(), password=form['password'].value())
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
    return rend(request, 'store/login.html', {'form': form})


def loggout(request):
    logout(request)
    return redirect('home')


def register(request):
    if request.user.__str__() != "AnonymousUser":
        return error(request, "Вы уже аутентифицированы")
    if request.method == "POST":
        if request.POST.get('new') == "false":
            return email(request, request.user)
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User()
            user.username = form['username'].value()
            user.password = form['password'].value()
            user.email = form['email'].value()
            user.first_name = form['first_name'].value()
            user.last_name = form['last_name'].value()
            user.date_of_birth = form['date_of_birth'].value()
            user.save()
            dj_user = DjangoUser(username=user.username, password=user.password)
            dj_user.save()
            login(request, dj_user)
            return email(request, user)
    else:
        form = RegisterForm()
    return rend(request, 'store/register.html', {'form': form})


def settings(request):
    return None


def reset_password(request):
    return None


def email(request, user=None):
    if user is not None:
        if not user.is_verify:
            user.tokenize()
            server = smtplib.SMTP()
            server.connect("smtp.gmail.com", 587)
            server.starttls()
            server.login("funnymanalex25@gmail.com", "3141592653589793AAATripple")
            multi_msg = MIMEMultipart('alternative')
            multi_msg['Subject'] = Header("Код для регистрации", "utf-8")
            multi_msg['From'] = Header("Бот Alex-Shop73", "utf-8")
            multi_msg['To'] = user.email
            html = """
                <h3>Вы были зарегистрированы на сайте интернет магазина Alex-Shop73<br>чтобы подтвердить регистрацию нажмите на кнопку<br><br></h3>
                <h4>Логин: <b>{0}</b></h4>
                <h4>Пароль: <b>{1}</b><br></h4>
                <a href="http://alexgames73.pythonanywhere.com/email?username={0}&token={2}" style="
                    border-radius: 4px;
                    -webkit-box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.2), 0 1px 2px rgba(0, 0, 0, 0.08);
                    -moz-box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.2), 0 1px 2px rgba(0, 0, 0, 0.08);
                    box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.2), 0 1px 2px rgba(0, 0, 0, 0.08);
                    color: #fff;
                    display:block;
                    width:200px;
                    text-align: center;
                    font-family: Arial, Helvetica, sans-serif;
                    font-size: 14px;
                    padding: 8px 16px;
                    margin: 20px auto;
                    text-decoration: none;
                    text-shadow: 0 1px 1px rgba(0, 0, 0, 0.075);
                    -webkit-transition: background-color 0.1s linear;
                    -moz-transition: background-color 0.1s linear;
                    -o-transition: background-color 0.1s linear;
                    transition: background-color 0.1s linear;
                    background-color: rgb( 43, 153, 91 );
                    border: 1px solid rgb( 33, 126, 74 );
                ">Подтвердить регистрацию</a>
            """.format(
                user.username,
                user.password,
                user.token
            )
            msg = MIMEText(html, 'html', 'utf-8')
            multi_msg.attach(msg)
            server.sendmail("funnymanalex25@gmail.com", user.email, multi_msg.as_string())
            server.quit()
        return rend(request, 'store/email.html', {'user': user})
    else:
        try:
            user = User.objects.get(username=request.GET.get("username"), token=request.GET.get("token"))
            if relativedelta(datetime.datetime.now(), user.last_tokenize).minutes < 5:
                if user.tokenize(check=True) == request.GET.get("token"):
                    user.is_verify = True
            return email(request, user)
        except Exception:
            return error(request, "Ссылка не действительна")
