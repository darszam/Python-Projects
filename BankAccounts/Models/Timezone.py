import numbers
from datetime import timedelta


class Timezone:
    def __init__(self, name, offset_hour, offset_minute):
        if (name is None) | (str(name).strip() == ''):
            raise ValueError("Name of timezone can't be empty")
        if not isinstance(offset_hour, numbers.Integral):
            raise TypeError("Offset hours must be integer")
        if not isinstance(offset_minute, numbers.Integral):
            raise TypeError("Offset minutes must be integer")
        if abs(offset_minute) > 59:
            raise ValueError("Minutes offset can't be greater than 59")

        offset = timedelta(hours=offset_hour, minutes=offset_minute)
        if (offset < timedelta(hours=-12, minutes=0)) | (offset > timedelta(hours=14, minutes=0)):
            raise ValueError("Offset must be between -12 hours and +14 hours")

        self._name = name
        self._offset = offset
        self._off_hour = offset_hour
        self._off_minute = offset_minute

    @property
    def offset_hours(self):
        return self._off_hour

    @property
    def offset_minutes(self):
        return self._off_minute

    @property
    def offset(self):
        return self._offset

    @property
    def name(self):
        return self._name

    def __repr__(self):
        return f"Timezone: {self.name}, offset hours: {self.offset_hours}, offset minutes: {self.offset_minutes}"
