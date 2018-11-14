import requests



def get_single_data():
    url = 'https://jsonplaceholder.typicode.com/posts/1'
    response = requests.get(url, None, headers={"Content-Type": "application/json"})
    return response.json()

def get_all_data():
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url, None, headers={"Content-Type": "application/json"})
    return response.json()

def post_data():
    url = 'https://jsonplaceholder.typicode.com/posts'
    data = '{"userId": 1, "title": "This is Nalin title.", "body": "This is Nalin body."}'
    response = requests.post(url, data, None, headers={"Content-Type": "application/json"})
    return response.json()

def update_data():
    singleData = get_single_data()
    print(singleData)
    id = str(singleData['id'])
    print(id)

    url = 'https://jsonplaceholder.typicode.com/posts/'+id

    data = '{"userId": 1, "id": 1, "title": "This is test title", "body":"This is test body."}'
    response = requests.put(url, data, headers={"Content-Type": "application/json"})
    return response.json()

def patch_data():
    singleData = get_single_data()
    print(singleData)
    id = str(singleData['id'])
    print(id)

    url = 'https://jsonplaceholder.typicode.com/posts/' + id

    data = '{"title": "This is new title."}'
    response = requests.patch(url, data, headers={"Content-Type": "application/json"})
    return response.json()
