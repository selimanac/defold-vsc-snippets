import os, json
import re

#path to your Defold API doc folder
path_to_json = '.' 

#dict for content
data = {} 

#get json files names from folder
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

#tags to remove from brief
TAG_RE = re.compile(r'<[^>]+>') 

#Remove html tags from brief
def remove_tags(text):
    return TAG_RE.sub('', text)

#Files loop
for _files in json_files: 
    json_file_name = _files
    json_file = json.loads(open(json_file_name).read()) #open file

    #elements loop
    for _method in json_file["elements"] :
        if _method["type"] == "MESSAGE":
             _i = 3
        else:
             _i = 1
        _ii = 1     
        _p_v = ""

        #parameters loop
        for _params in _method["parameters"] :
            if _ii == 1:
                _p_v = "${"+str(_i)+":" + _params["name"] + "}"
            else:    
                _p_v = _p_v +  ", ${"+str(_i)+":" + _params["name"] + "}"
        
            _i = _i+1
            _ii = _ii+1
           
        _new_key = _method["name"]
        _body=""

        #FUNCTION - MESSAGE - PROPERTY
        if _method["type"] == "FUNCTION":
            _body = _method["name"]+"("+_p_v+")"
        elif _method["type"] == "MESSAGE":
            if _p_v == "":
                _body = 'msg.post(${1:receiver}, "'+_method["name"]+'")'
            else:
                _body = 'msg.post(${1:receiver}, "'+_method["name"]+'", ${2:{'+_p_v+'\}})'
            
        elif _method["type"] == "PROPERTY":
            _body = '"'+_method["name"]+'"'    
        else:
            _body = _method["name"]
            
        #format snippets           
        _new_value = {
            "prefix": _method["name"],
            "body":   _body,
            "description": remove_tags(_method["brief"])
                }
        data[_new_key] = _new_value

  
#save to new file
with open('bin/data.json', 'w') as outfile:  
    json.dump(data, outfile)
