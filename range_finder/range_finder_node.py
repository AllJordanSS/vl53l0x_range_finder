import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
try:
    from .range_finder import RangeFinder
except Exception:
    from range_finder import RangeFinder
    
class RangeFinderNode(Node):
    def __init__(self):
        super().__init__('range_finder_node')

        # Carrega os parâmetros do arquivo YAML
        self.declare_parameters(
            namespace='',
            parameters=[
                ('min_distance', 49),                       # Distância do sensor até o chão (mm).
                ('max_distance', 2001),                     # O sensor funcona bem até 2m, acima disso há muito erro de leitura (mm).
                ('offset', -50),                            # Offset de leitura (valor não validado ainda)(mm)
                ('hole_threshold', 70),                     # Limite máximo, acima dele será considerado buraco(mm)
                ('check_interval', 0.2),                    # Frequência de leitura em (s)
                ('measurement_timing_budget', 200000),      # Tempo de medição em microssegundos(us)
                ('signal_rate_limit', 0.1),                 # Limite mínimo da taxa de sinal (s)
                ('debug', True)                             # Flag para logs
            ]
        )

        # Obtém os parâmetros
        self.min_distance = self.get_parameter('min_distance').value
        self.max_distance = self.get_parameter('max_distance').value
        self.offset = self.get_parameter('offset').value
        self.hole_threshold = self.get_parameter('hole_threshold').value
        self.check_interval = self.get_parameter('check_interval').value
        self.measurement_timing_budget = self.get_parameter('measurement_timing_budget').value
        self.signal_rate_limit = self.get_parameter('signal_rate_limit').value
        self.debug = self.get_parameter('debug').value  # Flag de debug

        # Inicializa o sensor com os parâmetros
        self.sensor = RangeFinder(
            min_distance=self.min_distance,
            max_distance=self.max_distance,
            offset=self.offset,
            measurement_timing_budget=self.measurement_timing_budget,
            signal_rate_limit=self.signal_rate_limit
        )

        # Cria um publisher para enviar a distância medida
        self.publisher_ = self.create_publisher(Float32, 'range_finder/distance', 10)

        # Timer para verificar a distância periodicamente
        self.timer = self.create_timer(self.check_interval, self.timer_callback)

    def log(self, level, message):
        """
        Método auxiliar para exibir logs apenas se a flag debug for True.
        """
        if not self.debug:
            return  # Sai da função sem registrar nada se debug for False

        if level == "info":
            self.get_logger().info(message)
        elif level == "warn":
            self.get_logger().warn(message)
        elif level == "error":
            self.get_logger().error(message)

    def timer_callback(self):
        # Lê a distância do sensor
        distance = self.sensor.get_distance()

        if distance is not None:
            # Publica a distância como uma mensagem Float32
            msg = Float32()
            msg.data = float(distance)
            self.publisher_.publish(msg)

            # Verifica se há um buraco
            if distance > self.hole_threshold:
                self.log("warn", f"⚠️ ALERTA: BURACO DETECTADO! Distância: {distance} mm")
            else:
                self.log("info", f"Chão normal detectado. Distância: {distance} mm")
        else:
            self.log("warn", "Leitura inválida, ignorando...")

def main(args=None):
    rclpy.init(args=args)
    node = RangeFinderNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()