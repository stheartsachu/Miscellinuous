import requests
data = requests.get("http://127.0.0.1:8000/api/users_list/",)
print((data.json())[-1])
d =  {
        "employee_id": 4,
        "employee_name": "panoo",
        "employee_age": 100,
        "employee_ranking": 2.0
    }
requests.post("http://127.0.0.1:8000/api/users_list/",data=d)
