from django.shortcuts import render
from pymongo import MongoClient



def search(request):

    return render(request,'search_fish/search.html')

def search_results(request):

    global db, results
    try:
        client = MongoClient('mongodb://user1:thsgPwls@localhost:27017')
        db = client['mul_db']
        print("MongoDB에 연결되었습니다.")
    except Exception as e:
        print("MongoDB에 연결할 수 없습니다.",e)

    collection = db['fishes']
    #print("collection도 접속됨")
    query = request.GET.get('q')
    #print(query)

    if not query:
        message = '검색어를 입력하시지 않으셨습니다. '
        return render(request, 'search_fish/search.html', {'message': message})

    else :
        try:
            results = collection.find({'fish_name': query})
            results = (list(results))

        except Exception as e:
            print(f'Query error: {str(e)}')

        return render(request, 'search_fish/fishinfo.html', {'results': results, "query": query})






