from django.http import HttpResponse
from django.shortcuts import render
from matplotlib.pyplot import title
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Articles, Authors
from .serializers import ArticleSerializer


###############################################################################

# def home(request):
#     return render('index.html')

###############################################################################

@api_view(['GET'])
def get_all_articles(request):
    
    articles = Articles.objects.all()
    
    result=[]  
    
    for i in articles:
        title = i.title
        content = i.content
        date = i.date

        authors_list = Authors.objects.filter(title = i)
        
        authors=[]
        
        for j in authors_list:
            authors.append(j.author)
        
        dict={
            'Title':title,
            'Content':content,
            'Date-Time':date,
            'Authors':authors
        }
        
        result.append(dict)
    
        
    return Response(result)


###############################################################################

@api_view(['GET'])
def get_article_by_name(request, pk):

    try:
        articles = Articles.objects.get(title=pk)
    except Articles.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND) 
    
    title = articles.title
    content = articles.content
    date = articles.date

    authors_list = Authors.objects.filter(title = title)
    
    authors=[]
    
    for j in authors_list:
        authors.append(j.author)
    
    dict={
        'Title':title,
        'Content':content,
        'Date-Time':date,
        'Authors':authors
    }
    
        
    return Response(dict)

###############################################################################

@api_view(['POST'])
def create_article(request):
    
    # {
    #     "title":"title-1",
    #     "content":"content-1",
    #     "author":"demo-author-1"
    # }
    
    if request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            
            data = serializer.validated_data
            print(data)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

###############################################################################

@api_view(['PUT'])
def update_article(request,pk):
    
    try:
        article = Articles.objects.get(pk=pk)
    except Articles.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


###############################################################################

@api_view(['DELETE'])
def delete_article(request,pk):
    
    try:
        article = Articles.objects.get(pk=pk)
    except Articles.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


###############################################################################