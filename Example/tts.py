import requests
import base64

api_key = "enter_your_own_google_api_key"

def SaveToTxt(file, data):
    fout = open(file, 'w')
    fout.write(data)
    fout.close()

def Base64_to_output(txt, output_file):
    fin = open(txt, 'r')
    base64_data = fin.read()
    fin.close()
    ori_image_data = base64.b64decode(base64_data)
    fout = open(output_file, 'wb')
    fout.write(ori_image_data)
    fout.close()

def TTS():
    text = "Hello.Maker fabs is a shenzhen company.Today is 2020/10/28.Now is rain. My name is Vincent."
    data = """
        {
            "input": {
                "text": "
                """+ text +"""
                "
            },
            "voice": {
                "languageCode": "en-gb",
                "name": "en-GB-Standard-A",
                "ssmlGender": "FEMALE"
            },
            "audioConfig": {
                "audioEncoding": "MP3"
            }
        }
    """
    headers = {'content-type': 'application/json'}

    r = requests.post(
        'https://texttospeech.googleapis.com/v1/text:synthesize?key='+api_key, data=data, headers=headers)
    #print(r.text)

    r_list = eval(r.text)

    #print(r_list["audioContent"])

    SaveToTxt("./tts_response.txt", str(r_list))
    SaveToTxt("./temp.txt", r_list["audioContent"])
    Base64_to_output("./temp.txt", "./output.mp3")

if __name__ == '__main__':
    TTS()
    # print(__name__)

