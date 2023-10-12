
def time_to_get():
    import datetime
    tim = datetime.datetime.now().strftime("%d.%m.%Y")
    return tim

def time_strart():
    import datetime
    dim = datetime.datetime.now().strftime("%H:%M:%S")
    return dim

def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

def time_closed():
    from datetime import datetime

    # record current timestamp
    start = datetime.now()

    # create loop-setup for testing
    a = 0
    for i in range(1000):
        a += (i**100)

    # record loop end timestamp
    end = datetime.now()

    # find difference loop start and end time and display
    td = (end - start).total_seconds() * 10**3

    return td
