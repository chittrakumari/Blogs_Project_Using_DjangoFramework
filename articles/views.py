from django.shortcuts import render
from  .models import Article
def article_list(request):
    
    articles=Article.objects.all().order_by('date')
    
    #we are passing a third parameter articles using dictionary or key-value pair 
    return render(request,'articles/article_list.html',{'articles':articles})
# Create your views here.
