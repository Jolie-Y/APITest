import requests

url="http://10.20.90.2/api/0/task"

json = {
    
  "act": "check",
  "detail": {
    "auth": "UnFAYJTU74pjLxICJ4ApBCwp9dtaBzyjjdQZErXeHkkxPRK7XZ1HiFC3B660uKGf",
    "meta": True
  }

}

re = requests.post(url,json=json)

print(re.json())



