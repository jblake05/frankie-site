import json
import os

def generateJSON():
    path = "C://Users//Jeff//Desktop//CS//frankie-site//src//lib//assets//ravelry"
    dir_list = os.listdir(path)
    # print(dir_list)

    jsonList = []

    for file in dir_list:
        title = file.replace("_", " ").title()[:file.index(".")]
        jsonList.append(json.dumps({
            "slug": f"{file}",
            "title": title,
            "src": f"{file}",
            "description": "test"
        }))
    
    with open("./file.json", "w") as f:
        f.write("export const posts = [")
        for jsonObj in jsonList:
            f.write(jsonObj)
            f.write(",")
        f.write("]")

generateJSON()

# slug, title, src, description