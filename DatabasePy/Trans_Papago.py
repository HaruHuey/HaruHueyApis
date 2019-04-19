import json
import urllib.request

def Trans(text_t):
    # 접속자 ID
    client_id = "{{ CLIENT_ID }}"

    # 접속자 고유번호
    client_secret = "{{ CLIENT_SECRET }}"

    encText = urllib.parse.quote(text_t)

    # NMT 번역
    data = "source=ko&target=en&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)

    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    
    rescode = response.getcode()

    if (rescode == 200):
        response_body = response.read().decode('utf-8')
        trans_text = json.loads(response_body)["message"]["result"]["translatedText"]
        return trans_text

    else:
        return rescode