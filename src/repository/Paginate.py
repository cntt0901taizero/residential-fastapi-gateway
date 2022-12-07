from src.schemas.Paginator import Paginator


def paginate(data, page_num, page_size, total) -> Paginator:
    current_count = page_num * page_size
    response = {"data": data, "total": total, "count": len(data), "pagination": {}}

    if current_count >= total:
        response["pagination"]["next"] = False

        if page_num > 1:
            response["pagination"]["previous"] = True
        else:
            response["pagination"]["previous"] = False
    else:
        if page_num > 1:
            response["pagination"]["previous"] = True
        else:
            response["pagination"]["previous"] = False

        response["pagination"]["next"] = True
    paginator = Paginator.parse_obj(response)
    return paginator