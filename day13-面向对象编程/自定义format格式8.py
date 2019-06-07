# coding=utf-8

format_dict = {
    'ymd': '{0.year}{0.month}{0.day}',
    'y:m:d': '{0.year}:{0.month}:{0.day}',
    'y-m-d': '{0.year}-{0.month}-{0.day}'
}


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, format_spec):
        if not format_spec or format_spec not in format_dict:
            format_spec = 'ymd'
        fm = format_dict[format_spec]
        return fm.format(self)


date = Date(2018, 12, 30)
print(date.__format__('asdfsf'))  # 20181230
print(date.__format__('y:m:d'))  # 2018:12:30
