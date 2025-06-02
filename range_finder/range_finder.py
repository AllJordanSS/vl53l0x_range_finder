import time
import board
import busio
import adafruit_vl53l0x

class RangeFinder:
    def __init__(self, min_distance, max_distance, offset, measurement_timing_budget, signal_rate_limit):
        # Inicializa o sensor
        i2c = busio.I2C(board.SCL, board.SDA)
        self.sensor = adafruit_vl53l0x.VL53L0X(i2c)

        # Configurações do sensor
        self.sensor.measurement_timing_budget = measurement_timing_budget
        self.sensor.signal_rate_limit = signal_rate_limit

        # Parâmetros de filtragem
        self.min_distance = min_distance
        self.max_distance = max_distance
        self.offset = offset

    def get_distance(self):
        # Lê a distância e aplica o offset
        distance = self.sensor.range + self.offset
        if self.min_distance <= distance <= self.max_distance:
            return distance
        else:
            return None