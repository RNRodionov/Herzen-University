"""
Для вычисления дисперсии и ср. квадр. отклонения использовать 
https://myslide.ru/documents_3/b9d7b50c38e81a4b8b7645742d3b22c7/img10.jpg
"""


class MathStats():
    def __init__(self, file):
        import csv

        self._file = file
        self._data = []
        self._mean = None
        self._max = float('-Inf')
        self._min = float('Inf')
        with open(self._file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            for _r in reader:
                row = {
                    'Date': _r[''],
                    'Offline': float(_r['Offline Spend']),
                    'Online': float(_r['Online Spend']),
                }
                self._data.append(row)

    @property
    def data(self):
        return self._data

    @property
    def mean(self):
        """
        Вычисление среднего по оффлайн и онлайн тратам
        """

        sums = {'offline': 0, 'online': 0}
        for _l in self._data:
            sums['offline'] += _l['Offline']
            sums['online'] += _l['Online']

        self._mean = (sums['offline'] / len(self._data), sums['online'] / len(self._data))

        return self._mean

    @property
    def max(self):
        greaterNumberBetweenTwo = {'offline': 0, 'online': 0}
        for _l in self._data:
          if _l['Offline'] > greaterNumberBetweenTwo['offline']:
            greaterNumberBetweenTwo['offline'] = _l['Offline']
          if _l['Online'] > greaterNumberBetweenTwo['online']:
            greaterNumberBetweenTwo['online'] = _l['Online']
        self._max = (greaterNumberBetweenTwo['offline'], greaterNumberBetweenTwo['online'])
        return self._max

    @property
    def min(self):
        lesserNumberBetweenTwo = {'offline': -1, 'online': -1}
        for _l in self._data:
          if (_l['Offline'] < lesserNumberBetweenTwo['offline'] or lesserNumberBetweenTwo['offline'] < 0):
            lesserNumberBetweenTwo['offline'] = _l['Offline']
          if (_l['Online'] < lesserNumberBetweenTwo['online'] or lesserNumberBetweenTwo['online'] < 0):
            lesserNumberBetweenTwo['online'] = _l['Online']
        self._min = (lesserNumberBetweenTwo['offline'], lesserNumberBetweenTwo['online'])
        return self._min

    @property
    def disp(self):
        disps = {'offline': 0, 'online': 0}
        means = self.mean
        for _l in self._data:
            disps['offline'] += (_l['Offline'] - means[0])**2
            disps['online'] += (_l['Online'] - means[1])**2
        self._disp = (disps['offline'] / len(self._data), disps['online'] / len(self._data))
        return self._disp

    # по аналогии — со среднем квадратичным отклонением
    @property
    def sigma_sq(self):
        from math import sqrt
        disps = self.disp
        self._sigma_sq = (sqrt(disps[0]), sqrt(disps[1]))
        return self._sigma_sq
