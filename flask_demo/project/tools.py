import datetime

from project.models import Device


def switch_db_data(keywords, db_data):
    def get_dict_func(data):
        x = {}
        for i, j in zip(keywords, data):
            if isinstance(j, datetime.datetime):
                j = str(j)
            x[i] = j
        return x

    return list(map(get_dict_func, db_data.values(keywords)))


def get_all_data(keywords, page, num):
    db_origin = Device.query.filter(Device.name != "")

    data_count = db_origin.count()
    start = (page - 1) * num
    end = page * num
    if page or num:
        db_origin = db_origin.slice(start, end)
    data_list = switch_db_data(keywords, db_origin)
    data = {"data_count": data_count, "data_list": data_list}
    return data
