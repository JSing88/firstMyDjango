from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
import random

# 새로 생성되는 글의 번호를 위한 전역변수 
nextId = 4

# 자료구조 생성. for CRUD 
#  --> 리스트 [ ...딕셔너리 ]
topics = [
    {'id': 1,'title': 'routing', 'body': 'Routing is...'},
    {'id': 2,'title': 'view',    'body': 'View is...'},
    {'id': 3,'title': 'Model',   'body': 'Model is...'},
]

# id 값이 전달 안되었을때 기본값 'None'설정..
def HtmlTemplate(articleTag, id=None):

    global topics   # topics변수를 전역변수(Golbal) 지정
    contextUI = '' 

    if id != None: 
        contextUI = f'''
            <p>
                <form action="/delete/" method="post">
                    <input type="text" name="id" value="{id}">
                    <input type="submit" value="delete">
                </form>
            </p>
        '''
    
    ol = ''

    # f를 붙이면 중괄호{}로 변수를 바로 사용할 수 있다.
    # A href "링크"사용 Http GET방식.
    for tp in topics:
        ol += f'<li><a href="/read/{tp["id"]}">{tp["title"]}</a></li>'

    return f'''
    <html>
        <body>
            <h1><a href="/">Django</a></h1>
            <ul>
                {ol}
            </ul>
            {articleTag}
            <div>
                <br/><br/>
                <p><a style="background-color:black; color:white;" href="/create">Crate New</a></p>
                {contextUI}
            </div>
        </body>
    </html>
    '''


# Caution!: 함수의 첫번째 인자로는 Client의 요청정보를 담는 요청에 관련된 객체를선언한다. (통상적: Request객체)
def index(request):
    # HttpResponse: Client의 요청에 관련된 부분을 Http를 이용해서 응답을 하겠다는 의미 
    # return HttpResponse('Welcome MySecondApp')
    # return HttpResponse('<h1>Random</h1><br/>' + str(random.random()))

    article = '''
    <h2>Welcome</h2>
    Hello, Django
    '''

    return HttpResponse(HtmlTemplate(article))

def read(request, pageNo): 
    # url을 통하여 들어온 변수(pageNo)의 DataType은 문자열이다.

    global topics
    article = ''    # 상세내용을 리턴하기 위한. 변수 

    for tp in topics: 
        if tp['id'] == int(pageNo):
            article = f'<h2>{tp["title"]}</h2><br/>{tp["body"]}'

    return HttpResponse(HtmlTemplate(article, pageNo))

# 파이썬 장고에서 관리하는 보안감지를 피하기 위해 @csrf_exempt 사용
@csrf_exempt
def create(request): 

    global nextId

    print('Request Method --------------->', request.method)

    if request.method == 'GET':
        article = '''
            <form action="/create/" method="post">
                <p><input type="text" name="title" placeholder="제목입력.."></p>    
                <p><textarea          name="body" placeholder="본문입력.."></textarea></p>
                <p><input type="submit"></p>
            </form>
        '''
        # <p>태그-- 단락을 나타나는 태그, 줄바꿈 역할 
        # "submit" 을 하였을 시, Server로 보내야될 Path --> form-action

        # 제목에 api, 본문에 Api Exciting을 기재하고 Submit을 하였을시...
        # http://localhost:8000/create/?title=api&body=Api+Exciting
        return HttpResponse(HtmlTemplate(article)) 
    elif request.method == "POST":
        
        # Server로 전송한 값을 받기위해서는 POST
        print("Submit Value ==> ", request.POST)

        nwTtl = request.POST['title'] 
        nwBdy = request.POST['body']

        newTopic = {"id": nextId, "title": nwTtl,"body": nwBdy }
        topics.append(newTopic)

        moveUrl = '/read/' + str(nextId)

        # 글의 번호를 증가 (Sequence)
        nextId   = nextId + 1 

        return redirect(moveUrl)


## localhost:8000/read/1      -- Get PathVariable
## localhost:8000/read/?id=1  -- Get QueryString  
## Server의 자원을 변경할 시.. POST 사용

@csrf_exempt
def delete(request):

    global topics

    print('Client Request :', request.method)

    if request.method == "POST" :
        id = request.POST['id']
        print('Delete Target(id) -- ', id)

        newTopics = []

        for tp in topics:                 
            if tp['id'] != int(id):
                newTopics.append(tp) 
        
        topics = newTopics

        return redirect('/')
