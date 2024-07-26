import requests
import json
MAIN_URL="https://reqres.in/api/"

def get_support_text():
    api_url = "https://reqres.in/api/users"
    response = requests.get(api_url)
    data = response.json()
    support_text = data["support"]["text"]
    return support_text

def single_user():
    api_url = "https://reqres.in/api/users/2"
    response = requests.get(api_url)
    data = response.json()
    single_user_data = data["data"] 
    return single_user_data

     


def single_user_not_found(userid):
    #api_url = "https://reqres.in/api/users/23" #mevcut değil
    response = requests.get(url=MAIN_URL + "users/" + userid) 
    print(response.status_code)
    try:
        if (response.status_code == 404):
            print("Not Found !")
    except:
        data = response.json()
        single_user_data_not_found = data["data"] 
        return single_user_data_not_found
    


def create_user():
    #api_url = "https://reqres.in/api/users"
    username = input("Username = ")
    job = input("Job = ")
    
    veriler = {
        "username":username,
        "job":job
    }
    
    #verilers = json.dumps(veriler,indent=4)  #eklenen verileri gösterir
    
    response = requests.post(url=MAIN_URL + "users" ,json=veriler) #ekleme işlemi
    print(response.status_code)
    print(response.json())




def update_users():
    api_url = "https://reqres.in/api/users/2"
    
    username = input("Username = ")
    job = input("Job = ")
    veriler = {
        "username ": username,
        "job" : job
    }
    response = requests.put(api_url)    
    requests.put(api_url,json=veriler)
    if(response.status_code == 200):
        jsons = json.dumps(veriler,indent=4)  #eklenen verileri gösterir
        info = response.text
        print(jsons )
        print(info)



def register_user():
    api_url = "https://reqres.in/api/register"
      
    email = input("Your e-mail = ")
    password = input("Your password = ")
    veriler = {
        "email":email,
        "password" : password
    }

    response = requests.post(api_url,json=veriler)
    print(response.status_code) 
    print(response.json())
    


def login_succes():
    api_url = "https://reqres.in/api/login"
    
    email = input("Your e-mail = ")
    password = input("Your password = ")
    veriler = {
        "email":email,
        "password":password
    }

    response = requests.post(api_url,json=veriler)
    print(response.status_code)
    print(response.json())


 
def delete_user():
    api_url = "https://reqres.in/api/users/2"
    
    response = requests.delete(api_url)
    print(response)


def login_unsucces():
    api_url = "https://reqres.in/api/login"
    email = input("Your e-mail = ")
    veriler = {
        "e-mail": email
    }
    response = requests.post(api_url,json=veriler)
    print(response.status_code)
    print(response.json())



def delayed_response():
    api_url = "https://reqres.in/api/users?delay=3"
    response = requests.get(api_url)
    json_data = response.json()
    print(json_data)
    print(response.status_code)


# Ana program
if __name__ == "__main__":

    print(get_support_text())
    single_user = single_user()
    print(single_user)
    single_user_not_found()
    create_user()
    update_users()
    register_user()
    login_succes()
    login_unsucces()
    delayed_response()
    delete_user()
    print("End")