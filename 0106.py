import json
with open ("0106.json","r",encoding="utf8") as f:
    y = json.loads(f.read())
    print(y)
    
with open ("my.json","r") as f:
    y = json.loads(f.read())
    print(y)
    
with open("my.json","W") as fw:
    y = json.loads(fw.read())
    json.dump(my.json)
