from app.repository import vehicle_repo
from app.utilities.pagination import parsing_pagination, get_paging_config
from app.utilities.common import get_data_image
from app.utilities import upload


async def register_vehicle(db, user, house, data, images):
    vehicle = await vehicle_repo.register_vehicle(db, user, house, data)
    for image_name, image_data in images.items():
        if image_data:
            await upload.upload_image(image_data, 'tb_vehicle', vehicle.id, image_name)

    return vehicle
