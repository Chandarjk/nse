
# File for common utility

def form_res(data):
    res = {}
    if data:

        for key in data.keys():
            res[key] = data[key]
    return res