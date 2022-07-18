from entity.data import VolumeOrder


class Filter:
    def __init__(self, date, volumeOrder: VolumeOrder):
        self.date = date
        self.volumeOrder = volumeOrder
