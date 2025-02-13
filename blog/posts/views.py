from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
posts = [
    {
        'id':0,
        'title': 'Let\'s explore Py thon',
        'content': 'lorem ipsum'
    },
    {
        'id':1,
        'title': 'Let\'s explore JavaScript',
        'content': 'lorem ipsum'
    },
    {
        'id':2,
        'title': 'Django Framework',
        'content': 'lorem ipsum'
    }
]

def helloworld(request):
    return HttpResponse('<h1>Hello World </h1> <br>I´m testing this method')

def home(request):
    html = ' '
    for post in posts:
        html += f'''
            <div>
                <h1>{post['id']} - {post['title']}</h1>
                <p>{post['content']}</p>
            </div>'''
    return HttpResponse(html)

def post(request, id):
    for post in posts: 
        if post['id'] == id:
            post_dict = post
            break
    html = f'''
        <h1>{post_dict['title']}</h1>
        <p>{post_dict['content']}</p>
    '''
    return HttpResponse(html)
