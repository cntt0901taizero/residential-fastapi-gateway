from configs import get_settings


def get_data_image(data: list, model: str):
    result = []
    for item in data:
        image = f"{get_settings().residential_server_url}/web/image?model={model}&id={item.id}&field=image"
        item.image = image
        result.append(item)
    return result
