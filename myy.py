import json

with open("my.json","r") as f:
    y = json.loads(f.read())
    print(y)
    print(y["data"][0]["name"])#-하나만
    
    for item in y["data"]:#-계속 돌아감
        print(item["name"])
        
    for item in y["data"]:
        for i in range(len(item["family"]["siblings"])):
            print(item["family"]["siblings"][i]["name"])
            
    for item in y["data"]:
        for i in item["family"]["siblings"]:
            print(i["gender"])
            if i["gender"] == "M":
                print(i["name"]+"남자")
            else:
                print(i["name"]+"여자")
                
            
    # for item in y["data"]:
    #     for i in item.keys():
    #         print(i)
    
        
            
    
        
        
    