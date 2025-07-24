import datetime
from datetime import timezone, timedelta



timestamp_ms = 1729338087000

# 将毫秒时间戳转换为秒
timestamp = timestamp_ms / 1000

# 创建一个UTC时区
utc_timezone = timezone.utc

# 将时间戳转换为datetime对象，并指定为UTC时区
dt_utc = datetime.datetime.fromtimestamp(timestamp, utc_timezone)

# 北京时间比UTC快8小时，创建8小时的timedelta对象
beijing_timedelta = timedelta(hours=8)

# 将UTC时间转换为北京时间
dt_beijing = dt_utc + beijing_timedelta

# 格式化北京时间为字符串
beijing_time_str = dt_beijing.strftime('%Y-%m-%d %H:%M:%S')

print(f"北京时间: {beijing_time_str}")