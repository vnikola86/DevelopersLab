from datetime import datetime, time

def check_noise_schedule(cTime):

    if cTime < time(6,0) or (time(13,0) <= cTime <= time(17,0)) or cTime >= time(22,0):
        return "Workers are not allowed to make noise at this time."
    else:
        return "Workers are allowed to make noise at this time."

current_time = time(15, 0)

permission_message = check_noise_schedule(current_time)
print(permission_message)
