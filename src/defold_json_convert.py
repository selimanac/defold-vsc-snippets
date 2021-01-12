import os
import json
import re
import urllib
import shutil
from collections import defaultdict
import sys


def check_installation(rv):
    current_version = sys.version_info
    if current_version[0] == rv[0] and current_version[1] >= rv[1]:
        pass
    else:
        sys.stderr.write("[%s] - Error: Your Python interpreter must be %d.%d  (within major version %d)\n" %
                         (sys.argv[0], rv[0], rv[1], rv[0]))
        sys.exit(-1)
    return 0


# Calling the 'check_installation' function checks if Python is >= 2.7 and < 3
required_version = (2, 7)
check_installation(required_version)


def get_latest_version():
    url = "http://d.defold.com/stable/info.json"
    response = urllib.urlopen(url)
    if response.getcode() == 200:
        return json.loads(response.read())
    return {}


def download_file(url):
    print("Downloading %s" % url)
    tmpfile = '_dl.zip'
    os.system("wget -O %s %s" % (tmpfile, url))
    return tmpfile


def find_or_download_sdk(sha1):
    path = 'defolddocs/%s.zip' % sha1
    if os.path.exists(path):
        print("%s already downloaded" % path)
        return path

    print("%s not found. Downloading" % path)

    dirpath = os.path.dirname(path)
    if not os.path.exists(dirpath):
        print("Created directory %s" % dirpath)
        os.makedirs(dirpath)

    url = "http://d.defold.com/archive/%s/engine/share/ref-doc.zip" % sha1
    tmpfile = download_file(url)

    shutil.move(tmpfile, path)
    print("Downloaded %s" % path)
    return path


def unpack_file(path):
    unpack_path = os.path.join(os.path.dirname(path), sha1)
    if os.path.exists(unpack_path):
        return unpack_path
    print("Unpacking to %s" % unpack_path)
    os.system('unzip %s -d %s' % (path, unpack_path))
    return unpack_path


class element(object):
    def __init__(self, name):
        self.name = name


d = sha1 = get_latest_version()
sha1 = d.get('sha1', None)
print("Latest version is %s : %s" % (d.get('version', ''), sha1))

# Paths
path = find_or_download_sdk(sha1)
print("path: %s" % path)
unpack_path = unpack_file(path)
print("unpack_path: %s" % unpack_path)
docs_path = os.path.abspath(os.path.join(unpack_path, 'doc'))
print("docs_path: %s" % docs_path)

# path to your Defold API doc folder
path_to_json = docs_path

# dict for content
data = defaultdict(list)
dm_data = defaultdict(list)

# get json files names from folder
json_files = [pos_json for pos_json in os.listdir(
    path_to_json) if pos_json.endswith('.json')]

# tags to remove from brief
TAG_RE = re.compile(r'<[^>]+>')

# Remove html tags from brief


def remove_tags(text):
    return TAG_RE.sub('', text)


# Files loop
for _files in json_files:
    json_file_name = _files
    json_file = json.loads(
        open(path_to_json + "/" + json_file_name).read())  # open file

    # elements loop
    for _method in json_file["elements"]:
        if _method["type"] == "MESSAGE":
            _i = 3
        else:
            _i = 1
        _ii = 1
        _p_v = ""
        _p_v_temp = ""
        # parameters loop
        for _params in _method["parameters"]:
            if _ii == 1:
                _p_v = "${"+str(_i)+":" + _params["name"] + "}"
                _p_v_temp = _params["name"]
            else:
                _p_v = _p_v + ", ${"+str(_i)+":" + _params["name"] + "}"
                _p_v_temp = _p_v_temp + ", " + _params["name"]

            _i = _i+1
            _ii = _ii+1

        if _p_v_temp != "":
            _new_key = _method["name"] + "(" + _p_v_temp + ")"
        else:
            _new_key = _method["name"]

        _body = ""

        #FUNCTION - MESSAGE - PROPERTY
        if _method["type"] == "FUNCTION":
            _body = _method["name"]+"("+_p_v+")"
        elif _method["type"] == "MESSAGE":
            if _p_v == "":
                _body = 'msg.post(${1:receiver}, "'+_method["name"]+'")'
            else:
                _body = 'msg.post(${1:receiver}, "' + \
                    _method["name"]+'", ${2:{'+_p_v+'\}})'

        elif _method["type"] == "PROPERTY":
            _body = '"'+_method["name"]+'"'
        else:
            _body = _method["name"]

        # format snippets
        _new_value = {
            "prefix": _new_key,
            "body":   _body,
            "description": remove_tags(_method["brief"])
        }

        if "dm" in json_file_name or "shared" in json_file_name:
            dm_data[_new_key].append(_new_value)
            dict(dm_data)
        else:
            data[_new_key].append(_new_value)
            dict(data)

dir_path = os.path.abspath(os.path.join(unpack_path, 'bin'))
if not os.path.exists(dir_path):
    print("Created directory %s" % dir_path)
    os.makedirs(dir_path)
# save to new file
with open(dir_path + '/defold-snippets.json', 'w') as outfile:
    json.dump(data, outfile)

with open(dir_path + '/defold-dm-snippets.json', 'w') as outfile:
    json.dump(dm_data, outfile)
