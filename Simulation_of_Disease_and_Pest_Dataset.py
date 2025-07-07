import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os
import json

# ---------------------- 新增用户配置交互模块 ----------------------
def get_user_config():
    """获取用户输入的配置参数"""
    print("=== 果园病虫害数据集生成配置向导 ===")
    use_existing = input("是否使用已有的配置文件？(y/n, 默认n): ").strip().lower()

    config = {}
    if use_existing in ['y', 'yes']:
        config_path = input("请输入配置文件路径（默认config/config.json）: ").strip() or "config/config.json"
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print("配置文件不存在，将使用新配置")

    # 日期范围配置
    start_date_str = input("请输入起始日期（格式YYYY-MM-DD，默认2023-05-20）: ").strip() or "2023-05-20"
    end_date_str = input("请输入结束日期（格式YYYY-MM-DD，默认2025-05-20）: ").strip() or "2025-05-20"

    # 温度模拟参数（季节划分）
    print("\n--- 温度模拟参数 ---")
    summer_temp = list(map(float, input("夏季（6-8月）温度均值和标准差（默认28 3）: ").strip().split() or [28, 3]))
    winter_temp = list(map(float, input("冬季（12-2月）温度均值和标准差（默认5 3）: ").strip().split() or [5, 3]))
    other_temp = list(map(float, input("春秋季（其他月份）温度均值和标准差（默认18 3）: ").strip().split() or [18, 3]))

    # 湿度模拟参数
    print("\n--- 湿度模拟参数 ---")
    humidity_params = list(map(float, input("湿度正态分布均值和标准差（默认60 10）: ").strip().split() or [60, 10]))

    # 降雨量模拟参数
    print("\n--- 降雨量模拟参数 ---")
    rain_prob = float(input("降雨概率（0-1之间，默认0.2）: ").strip() or 0.2)
    rain_exp = float(input("降雨时的指数分布参数（默认5）: ").strip() or 5)

    # 输出配置
    config = {
        "date_range": {
            "start": start_date_str,
            "end": end_date_str
        },
        "temperature": {
            "summer": summer_temp,   # [mean, std]
            "winter": winter_temp,
            "other": other_temp
        },
        "humidity": {
            "mean": humidity_params[0],
            "std": humidity_params[1]
        },
        "rainfall": {
            "probability": rain_prob,
            "exponential_lambda": rain_exp
        }
    }

    # 保存配置到config目录
    config_dir = "config"
    if not os.path.exists(config_dir):
        os.makedirs(config_dir, exist_ok=True)
    config_path = os.path.join(config_dir, "config.json")
    with open(config_path, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=2, ensure_ascii=False)
    print(f"配置已保存到 {config_path}")

    return config

# ---------------------- 原有代码修改部分 ----------------------
# 加载用户配置（替换原固定参数）
user_config = get_user_config()

# 生成日期范围（使用用户配置）
start_date = datetime.strptime(user_config["date_range"]["start"], "%Y-%m-%d")
end_date = datetime.strptime(user_config["date_range"]["end"], "%Y-%m-%d")
date_range = pd.date_range(start=start_date, end=end_date)

# 初始化空列表来存储数据（原有代码不变）
dates = []
temperatures = []
humidities = []
rainfalls = []
pest_diseases = []

# 读取病虫害发生条件的 JSON 文件（原有代码不变）
data_dir = 'data'
json_path = os.path.join(data_dir, 'pest_conditions.json')
if not os.path.exists(data_dir):
    os.makedirs(data_dir, exist_ok=True)
try:
    with open(json_path, 'r', encoding='utf-8') as f:
        pest_conditions = json.load(f)
except FileNotFoundError:
    raise FileNotFoundError(
        f"关键配置文件缺失！请在 {json_path} 路径下创建 pest_conditions.json 文件。\n"
        "示例内容（可根据需要修改）:\n"
        '{"蚜虫": {"temperature_range": [15, 30], "humidity_range": [40, 80], "rainfall_range": [0, 5], "probability": 0.3}}'
    )

def check_condition(value, condition_range):  # 原有函数不变
    min_val, max_val = condition_range
    if min_val is not None and value < min_val:
        return False
    if max_val is not None and value > max_val:
        return False
    return True

# 模拟气象数据和病虫害发生情况（修改温度/湿度/降雨模拟逻辑）
for date in date_range:
    # 模拟温度（使用用户配置的季节参数）
    if date.month in [6, 7, 8]:  # 夏季
        temperature = np.random.normal(user_config["temperature"]["summer"][0], user_config["temperature"]["summer"][1])
    elif date.month in [12, 1, 2]:  # 冬季
        temperature = np.random.normal(user_config["temperature"]["winter"][0], user_config["temperature"]["winter"][1])
    else:  # 春秋季
        temperature = np.random.normal(user_config["temperature"]["other"][0], user_config["temperature"]["other"][1])
    temperature = max(0, temperature)  # 确保温度不低于 0

    # 模拟湿度（使用用户配置的参数）
    humidity = np.random.normal(user_config["humidity"]["mean"], user_config["humidity"]["std"])
    humidity = max(0, min(100, humidity))  # 确保湿度在 0 - 100 之间

    # 模拟降雨量（使用用户配置的参数）
    if np.random.rand() < user_config["rainfall"]["probability"]:  # 用户自定义降雨概率
        rainfall = np.random.exponential(user_config["rainfall"]["exponential_lambda"])  # 用户自定义指数参数
    else:
        rainfall = 0

    # 记录当日发生的病虫害（原有逻辑不变）
    daily_pest_diseases = []
    for pest_name, condition in pest_conditions.items():
        temp_check = check_condition(temperature, condition["temperature_range"])
        humidity_check = check_condition(humidity, condition["humidity_range"])
        rainfall_check = check_condition(rainfall, condition["rainfall_range"])
        probability_check = np.random.rand() < condition["probability"]
        if temp_check and humidity_check and rainfall_check and probability_check:
            daily_pest_diseases.append(pest_name)
    pest_disease_str = ', '.join(daily_pest_diseases) if daily_pest_diseases else "无"

    # 添加数据到列表（原有代码不变）
    dates.append(date)
    temperatures.append(temperature)
    humidities.append(humidity)
    rainfalls.append(rainfall)
    pest_diseases.append(pest_disease_str)

# 创建并保存 DataFrame（原有代码不变）
data = {
    '日期': dates,
    '温度 (°C)': temperatures,
    '湿度 (%)': humidities,
    '降雨量 (mm)': rainfalls,
    '病虫害': pest_diseases
}
df = pd.DataFrame(data)
df.to_csv('orchard_pest_disease_dataset.csv', index=False)
print("三年的果园病虫害数据集已生成并保存为 orchard_pest_disease_dataset.csv")