
---

# 📦 VL53L0X Range Finder ROS 2 Package

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

Este pacote ROS 2 permite ler dados de distância do sensor **VL53L0X** (sensor a laser infravermelho de curto alcance) e publicar esses dados como uma mensagem no sistema ROS 2. Além disso, ele implementa detecção básica de **buracos ou obstáculos**, com base em um limiar configurável. O pacote foi usado para uma detecção de buracos básica em uma plataforma robótica.

🔗 [Repositório no GitHub](https://github.com/AllJordanSS/vl53l0x_range_finder.git)

---

## 🧰 Funcionalidades

- ✅ Leitura de distância via I²C do sensor **VL53L0X**
- 🛠️ Configurações ajustáveis via parâmetros ROS 2
- 📡 Publicação da distância medida em um tópico ROS 2: `/range_finder/distance`
- ⚠️ Detecção de buracos com base em um threshold
- 📋 Logs detalhados (ativáveis/desativáveis)
- 🔄 Fácil integração com outros nós ROS 2

---

## 🧪 Tópicos Publicados

| Tópico | Tipo | Descrição |
|--------|------|-----------|
| `/range_finder/distance` | `std_msgs/Float32` | Distância medida pelo sensor em milímetros |

---

## ⚙️ Parâmetros Configuráveis

Os seguintes parâmetros podem ser configurados no launch file ou via arquivo `.yaml`:

| Parâmetro | Tipo | Padrão | Descrição |
|----------|------|--------|-----------|
| `min_distance` | int | 49 | Limite mínimo de leitura (mm) |
| `max_distance` | int | 2001 | Limite máximo de leitura (mm) |
| `offset` | int | -50 | Correção de desvio na leitura (mm) |
| `hole_threshold` | int | 70 | Limiar acima do qual considera-se haver um buraco (mm) |
| `check_interval` | float | 0.2 | Intervalo entre leituras (segundos) |
| `measurement_timing_budget` | int | 200000 | Tempo de medição em microssegundos |
| `signal_rate_limit` | float | 0.1 | Taxa mínima de sinal aceitável |
| `debug` | bool | True | Habilita ou desabilita logs informativos |

---

## 📦 Estrutura Atual do Pacote

```
vl53l0x_range_finder/
├── launch/
│   └── range_finder_launch.py        # Arquivo de lançamento ROS 2
├── package.xml                         # Metadados do pacote ROS 2
├── range_finder/
│   ├── __init__.py                     # Inicialização do módulo Python
│   ├── __pycache__/                    # Cache do Python
│   ├── range_finder_node.py            # Nó principal do ROS 2
│   └── range_finder.py                 # Driver do sensor VL53L0X
├── readme.md                           # Este arquivo
├── resource/
│   └── range_finder                    # Recursos adicionais
├── settings/
│   └── setting.yaml                    # Configurações personalizadas
├── setup.cfg                           # Configurações do setuptools
├── setup.py                            # Script de instalação
└── test/
    ├── test_copyright.py               # Teste de copyright
    ├── test_flake8.py                  # Validação de estilo de código
    └── test_pep257.py                  # Validação de docstrings
```

---

## 🔧 Requisitos

- Placa compatível com **I²C** (ex: Raspberry Pi, Jetson Nano)
- Sensor **VL53L0X** conectado corretamente
- Sistema com **ROS 2 (Iron/Irrelevant ou superior recomendado)**

### Dependências

```bash
sudo apt install python3-rpi.gpio python3-smbus
pip install adafruit-circuitpython-vl53l0x
```

---

## 🚀 Como Usar

1. Clone o repositório no seu workspace ROS 2:

```bash
cd ~/your_ros_workspace/src
git clone https://github.com/AllJordanSS/vl53l0x_range_finder.git
```

2. Compile o workspace:

```bash
cd ..
colcon build --packages-select vl53l0x_range_finder
source install/setup.bash
```

3. Execute o nó:

```bash
ros2 run vl53l0x_range_finder range_finder_node
```

Ou use o launch file:

```bash
ros2 launch vl53l0x_range_finder range_finder_launch.py
```

---

## 📈 Visualização das Dados

Para visualizar as distâncias medidas:

```bash
ros2 topic echo /range_finder/distance
```
---

## 👥 Contribuição

Contribuições são bem-vindas! Abra uma *issue* ou envie um *pull request* no GitHub.

---

## 📬 Contato

Se você tiver dúvidas, sugestões ou encontrar algum problema, abra uma issue no repositório ou entre em contato!

---
