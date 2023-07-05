def noneOrEmpty(obj:any)->bool:
    if isinstance(obj,int):
        return int(obj) == 0
    return obj is None