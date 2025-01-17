from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpResponseNotFound
from django.views.generic import View, ListView, DetailView
from store.forms import LoginForm, CheckoutForm
from store.models import LoginModel, ArticleModel, TagModel, CheckoutModel
from django.contrib.auth import authenticate
from django.db.models import Sum, Count, F
from django.template.loader import render_to_string
# Create your views here.

class LoginView(View):
    def get(self, request):
        login_model = LoginModel.objects.all()
        login_form = LoginForm(request.POST)
        
        context = {
            "login_model": login_model,
            "login_form": login_form
        }
        
        return render(request, "store/login.html", context)
    
    def post(self, request):
        login_model = LoginModel.objects.all()
        login_form = LoginForm(request.POST)
        
        if login_form.is_valid():
            login_form.save()
            
        context = {
            "login_model": login_model,
            "login_form": login_form
        }
        
        return render(request, "store/login.html", context)
    
class StartingPageView(View):
    def get(self, request):
        article_model = ArticleModel.objects.filter(tag=5)
        
        context = {
            "model": article_model
        }
        
        return render(request, "store/startingpage.html", context)
    
    def post(self, request):
        article_model = ArticleModel.objects.filter(tag=5)
        
        context = {
            "model": article_model
        }
        
        return render(request, "store/startingpage.html", context)
    
class MalePage(View):
    def get(self, request):
        article_model = ArticleModel.objects.filter(tag=1)
        
        context = {
            "article_model": article_model
        }
        
        return render(request, "store/male.html", context)
    
    def post(self, request):
        article_model = ArticleModel.objects.all()
        
        context = {
            "article_model": article_model
        }
        
        return render(request, "store/male.html", context)
    
class FemalePage(View):
    def get(self, request):
        article_model = ArticleModel.objects.filter(tag=2)
        
        context = {
            "article_model": article_model
        }
        
        return render(request, "store/female.html", context)
    
    def post(self, request):
        article_model = ArticleModel.objects.all()
        
        context = {
            "article_model": article_model
        }
        
        return render(request, "store/female.html", context)
    
class KidsPage(View):
    def get(self, request):
        article_model = ArticleModel.objects.filter(tag=4)
        
        context = {
            "article_model": article_model
        }
        
        return render(request, "store/kids.html", context)
    
    def post(self, request):
        article_model = ArticleModel.objects.all()
        
        context = {
            "article_model": article_model
        }
        
        return render(request, "store/kids.html", context)
    
class SportsPage(View):
    def get(self, request):
        article_model = ArticleModel.objects.filter(tag=3)
        
        context = {
            "article_model": article_model
        }
        
        return render(request, "store/sports.html", context)
    
    def post(self, request):
        article_model = ArticleModel.objects.all()
        
        context = {
            "article_model": article_model
        }
        
        return render(request, "store/sports.html", context)
    
class MaleDetailPage(DetailView):
    template_name = "store/maledetail.html"
    model = ArticleModel
    context_object_name = "models"
    
class FemaleDetailPage(DetailView):
    template_name = "store/femaledetail.html"
    model = ArticleModel
    context_object_name = "models"
    
class KidsDetailPage(DetailView):
    template_name = "store/kidsdetail.html"
    model = ArticleModel
    context_object_name = "models"
    
class SportsDetailPage(DetailView):
    template_name = "store/sportsdetail.html"
    model = ArticleModel
    context_object_name = "models"
    
class FavouritePage(View):
    def get(self, request):
        stored_articles = request.session.get("stored_articles")
        
        context = {}
        
        if stored_articles is None or len(stored_articles) == 0:
            context["articles"] = []
            context["has_articles"] = False
        else:
            articles = ArticleModel.objects.filter(id__in=stored_articles)
            context["articles"] = articles
            context["has_articles"] = True
            
        return render(request, "store/favourites.html", context)
    
    def post(self, request):
        stored_articles = request.session.get("stored_articles")
        
        if stored_articles is None:
            stored_articles = []
            
        article_id = int(request.POST["article_id"])
        
        if article_id not in stored_articles:
            stored_articles.append(article_id)
        else:
            stored_articles.remove(article_id)
            
        request.session["stored_articles"] = stored_articles
            
        return HttpResponseRedirect("/startingpage")
    
class AddToBag(View):
    def get(self, request):
        stored_buys = request.session.get("stored_buys")
        
        context = {}
        
        if stored_buys is None or len(stored_buys) == 0:
            context["buys"] = []
        else:
            articles = ArticleModel.objects.filter(id__in=stored_buys)
            context["buys"] = articles
            
        return render(request, "store/buys.html", context)
    
    
    def post(self, request):
        stored_buys = request.session.get("stored_buys")
        
        if stored_buys is None:
            stored_buys = []
            
        article_id = int(request.POST["article_id"])
        
        if article_id not in stored_buys:
            stored_buys.append(article_id)
        else:
            stored_buys.remove(article_id)
            
        request.session["stored_buys"] = stored_buys
            
        return HttpResponseRedirect("/startingpage")
    
class Help(DetailView):
    def get(self, request):
        return render(request, "store/help.html")
    
class ContactUs(DetailView):
    def get(self, request):
        return render(request, "store/contactus.html")
    
class BagView(View):
    def get(self, request):
        stored_in_the_bag = request.session.get("stored_in_the_bag")
        
        context = {}
        
        if stored_in_the_bag is None or len(stored_in_the_bag) == 0:
            context["articles"] = []
            context["has_articles"] = False
        else:
            articles = ArticleModel.objects.filter(id__in=stored_in_the_bag)
            context["articles"] = articles
            context["has_articles"] = True
            
        summ = []
            
        for article in articles:
            total = article.price
            summ.append(total)
            
        get_sum = sum(summ)
            
        context["sum"] = str(get_sum) 
            
        return render(request, "store/bag.html", context)
    
    def post(self, request):
        stored_in_the_bag = request.session.get("stored_in_the_bag")
        
        if stored_in_the_bag is None:
            stored_in_the_bag = []
            
        article_id = int(request.POST["article_id"])
        
        if article_id not in stored_in_the_bag:
            stored_in_the_bag.append(article_id)
        else:
            stored_in_the_bag.remove(article_id)
            
        request.session["stored_in_the_bag"] = stored_in_the_bag
            
        return HttpResponseRedirect("/startingpage")

class CheckoutView(View):
    def delete(self, request):
        del request.session["stored_in_the_bag"]
        return HttpResponseRedirect("startingpage")
    
    def get(self, request):
        checkout_model = CheckoutModel.objects.all()
        checkout_form = CheckoutForm(request.POST)
        stored_in_the_bag = request.session.get("stored_in_the_bag")
        articles = ArticleModel.objects.filter(id__in=stored_in_the_bag)
        
        summ = []
            
        for article in articles:
            total = article.price
            summ.append(total)
            
        get_sum = sum(summ)
        
        context = {
            "checkout_model": checkout_model,
            "checkout_form": checkout_form,
            "sum": str(get_sum),
            "delete": self.delete(request)
        }
        
        return render(request, "store/checkout.html", context)
    
    def post(self, request):
        checkout_model = CheckoutModel.objects.all()
        checkout_form = CheckoutForm(request.POST)
        
        if checkout_form.is_valid():
            checkout_form.save()
            
        context = {
            "checkout_model": checkout_model,
            "checkout_form": checkout_form
        }
        
        return render(request, "store/checkout.html", context) 