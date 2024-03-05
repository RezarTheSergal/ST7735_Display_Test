import datetime as dt


def debug_log(log, action="DEBUG"):
    log_time_dt = dt.datetime.utcnow()
    print(log_time_dt.date(), str(log_time_dt.time()).split('.')[0], "- " + action + ":",  log)
