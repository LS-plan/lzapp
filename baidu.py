import base64
import urllib
import requests

API_KEY = "mHf2t2zWFVubxjjIX1rXMuET"
SECRET_KEY = "nKacbGoVXByDFEyhL9RvaTRIexDc3ik4"


def tunn():
    url = "https://aip.baidubce.com/rest/2.0/ocr/v1/license_plate?access_token=" + get_access_token()

    # image 可以通过 get_file_content_as_base64("C:\fakepath\R-C.png",True) 方法获取
    # image = get_file_content_as_base64(image_input_fullname).replace('/', '%2F').replace('=', '%3D').replace('+', '%2B')
    image = get_file_content_as_base64(r"static/test.jpg").replace('/', '%2F').replace('=', '%3D').replace('+', '%2B')

    payload = 'image=' + image

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    # print(response.text)
    return response.json()


def get_file_content_as_base64(path, urlencoded=False):
    """
    获取文件base64编码
    :param path: 文件路径
    :param urlencoded: 是否对结果进行urlencoded
    :return: base64编码信息
    """
    with open(path, "rb") as f:
        content = base64.b64encode(f.read()).decode("utf8")
        if urlencoded:
            content = urllib.parse.quote_plus(content)
    return content


def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))


if __name__ == '__main__':
    tunn()
