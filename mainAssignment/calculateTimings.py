from datetime import datetime,timedelta


def addTime(time_str, minu, hr):
    given_time = datetime.strptime(time_str,'%H:%M:%S')
    update_time = given_time + timedelta(hours=hr, minutes=minu)
    updated_time = update_time.time()
    return updated_time


def calTime(shows,time,gap,interval,length):
    gap = int(gap)
    len_s = length.split(":")
    minutes = int(interval) + int(len_s[-1])
    hr = int(len_s[0])
    timings = ""

    for i in range(int(shows)):
        movie_time = addTime(time, minutes, hr)
        timings += str(time) + "-" + str(movie_time) + ",\n"
        movie_time = str(movie_time)
        time1 = addTime(movie_time, gap, hr=0)
        time = str(time1)

    return timings
