def sameparity(item=[]):
    l = []

    if item:
        r = item[0] % 2
        l.append(item[0])

        for i in item[1:]:
            if i % 2 == r:
                l.append(i)

    return l