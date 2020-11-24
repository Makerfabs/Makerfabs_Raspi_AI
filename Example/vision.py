import requests
import base64
import os


api_key = "enter_your_own_google_api_key"


def get_file_name(file_dir):
    file_list = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            #if os.path.splitext(file)[1] == '.jpeg':
                file_list.append(os.path.join(root, file))
    return file_list


def ToBase64(file):
    fin = open(file, 'rb')
    data = fin.read()
    base64_data = base64.b64encode(data)
    fin.close()
    return str(base64_data, encoding='UTF-8')
    # return base64_data

def ResultToJson(list):

    pass


def VISION(filename):
    image_data = ToBase64(filename)
    print(filename + "")

    #api_type = "LABEL_DETECTION"    #label
    api_type = "TEXT_DETECTION"    #ORC

    data = "{\"requests\":[{\"image\":{\"content\":\"" + image_data + \
        "\"},\"features\":[{\"type\":\"" + api_type +"\",\"maxResults\":5}]}]}"

    

    headers = {'content-type': 'application/json'}

    r = requests.post(
        'https://vision.googleapis.com/v1/images:annotate?key='+api_key, data=data, headers=headers)

    print(r.text)

    r_list = eval(r.text)

    if api_type == "LABEL_DETECTION" :
        result_list = r_list["responses"][0]["labelAnnotations"]
        #print(result_list)
        for result in result_list:
            print("    " + result["description"])
    
    if api_type == "TEXT_DETECTION" :
        result = r_list["responses"][0]["textAnnotations"][0]["description"]
        print(result)


if __name__ == '__main__':
    """
    for filename in get_file_name(".pic/"):
        VISION(filename)
    """
    VISION("./Example/test.jpg")
    # print(__name__)
