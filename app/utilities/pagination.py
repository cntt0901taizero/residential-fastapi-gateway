from math import ceil

from app.schemas.common import PageOutput, SearchPageInput, Paging


def parsing_pagination(data, total, config: SearchPageInput):
    total_pages = ceil(total / config.page_size) if total is not None else None
    return PageOutput(
        list_data=data,
        total_items=total,
        page_size=config.page_size,
        total_pages=total_pages,
        current_page=config.current_page
    )


def get_paging_config(config: SearchPageInput):
    page = config.current_page - 1 if config.current_page - 1 > 0 else 0
    offset = page * config.page_size

    return Paging(
        limit=config.page_size,
        offset=offset
    )
