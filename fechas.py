import datetime

my_time = datetime.datetime.now()

print(my_time.strftime('%H:%M'))

# %Y Year
# %m Month
# %d Day
# %H Hour
# %M Minute
# %S Secons

# %I Para no trabajar en formato 24 horas, osea: %H = 20  =>  %I = 08