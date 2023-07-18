def capitalize_nested(t):
    res = []
    for s in t:
        if type(s) == list:
            res.append(capitalize_nested(s))
        else:
            res.append(s.capitalize())
    return res


def capitalize_nested(t):
    if isinstance(t, list):
        return [capitalize_nested(s) for s in t]
    else:
        return t.capitalize()