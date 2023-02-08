import requests
import json

from config import get_settings


async def change_password(data, sid):
    auth_url = get_settings().residential_server_url + '/api/users/update_password'
    cookies = {'session_id': sid}
    headers = {'Content-type': 'application/json', 'X-Openerp': sid}
    json_obj = {
            "jsonrpc": "2.0",
            "params": {
                "old": data.old_password,
                "new1": data.new_password,
                "new2": data.confirm_password,

            }
        }
    rs = requests.post(url=auth_url, json=json_obj, cookies=cookies, headers=headers)
    return json.loads(rs.text)
