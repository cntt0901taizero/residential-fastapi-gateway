import base64
import json

import requests

from configs import get_settings


async def upload_image(image, model: str, model_id: int, field: str = "image"):
    file_content = await image.read()
    file_content = base64.b64encode(file_content).decode()
    url = get_settings().residential_server_url + '/api/upload'
    headers = {'Content-type': 'application/json'}
    json_obj = {
        "jsonrpc": "2.0",
        "method": "call",
        "params": {
            "name": image.filename,
            "mimetype": image.content_type,
            "res_id": model_id,
            "res_model": model,
            "res_field": field,
            "datas": file_content
        }
    }
    rs = requests.post(url=url, json=json_obj, headers=headers)
    rs = json.loads(rs.text)
    return rs
