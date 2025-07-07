# 果园病虫害数据集模拟项目

## 项目概述
本项目旨在模拟生成果园病虫害数据集，通过用户配置的气象参数（如日期范围、温度、湿度、降雨量等），结合病虫害发生的条件，模拟一段时间内果园的气象数据和病虫害发生情况，并将结果保存为 CSV 文件。

病虫害数据来源于《现代苹果病虫害防控技术》《中国苹果病虫害原色图鉴》，包含苹果生产中常见的病虫害及其发生条件。

## 项目结构果园病虫害数据集模拟/
├── data/
│   └── pest_conditions.json
├── config/
│   └── config.json
├── .idea/
│   ├── .gitignore
│   ├── modules.xml
│   ├── workspace.xml
│   ├── MarsCodeWorkspaceAppSettings.xml
│   ├── inspectionProfiles/
│   │   └── profiles_settings.xml
│   └── misc.xml
├── Simulation_of_Disease_and_Pest_Dataset.py
└── orchard_pest_disease_dataset.csv （生成的数据集）
### 各文件说明
- `data/pest_conditions.json`：包含各种病虫害发生的条件，如温度范围、湿度范围、降雨量范围和发生概率。数据来源于《现代苹果病虫害防控技术》《中国苹果病虫害原色图鉴》。
- `config/config.json`：用户配置文件，保存用户输入的日期范围、温度、湿度和降雨量的模拟参数。
- `.idea/`：IntelliJ IDEA 的项目配置文件目录。
- `Simulation_of_Disease_and_Pest_Dataset.py`：主程序文件，负责获取用户配置、模拟气象数据和病虫害发生情况，并生成数据集。
- `orchard_pest_disease_dataset.csv`：生成的果园病虫害数据集文件。

## 环境要求
- Python 3.x
- 依赖库：`pandas`、`numpy`

## 安装依赖
在项目根目录下，打开终端并执行以下命令安装所需的依赖库：pip install pandas numpy
## 使用方法
### 运行程序
在项目根目录下，打开终端并执行以下命令运行主程序：python Simulation_of_Disease_and_Pest_Dataset.py
### 配置向导
运行程序后，会出现配置向导，引导你输入相关参数：
1. **是否使用已有的配置文件**：输入 `y` 或 `yes` 表示使用已有的配置文件，输入 `n` 表示使用新配置。
2. **日期范围配置**：输入起始日期和结束日期，格式为 `YYYY-MM-DD`，默认值分别为 `2023-05-20` 和 `2025-05-20`。
3. **温度模拟参数**：分别输入夏季（6 - 8 月）、冬季（12 - 2 月）和春秋季的温度均值和标准差，默认值分别为 `[28, 3]`、`[5, 3]` 和 `[18, 3]`。
4. **湿度模拟参数**：输入湿度正态分布的均值和标准差，默认值为 `[60, 10]`。
5. **降雨量模拟参数**：输入降雨概率（0 - 1 之间）和降雨时的指数分布参数，默认值分别为 `0.2` 和 `5`。

### 保存配置
配置完成后，程序会将配置保存到 `config/config.json` 文件中，方便下次使用。

### 生成数据集
程序会根据用户配置模拟气象数据和病虫害发生情况，并将结果保存为 `orchard_pest_disease_dataset.csv` 文件。

## 数据集格式
生成的数据集包含以下列：
- `日期`：日期信息，格式为 `YYYY-MM-DD`。
- `温度 (°C)`：当日的模拟温度，单位为摄氏度。
- `湿度 (%)`：当日的模拟湿度，单位为百分比。
- `降雨量 (mm)`：当日的模拟降雨量，单位为毫米。
- `病虫害`：当日发生的病虫害名称，多个病虫害用逗号分隔，若无病虫害则显示 `无`。

## 病虫害数据来源
本项目中的病虫害数据来源于以下书籍：
- 《现代苹果病虫害防控技术》
- 《中国苹果病虫害原色图鉴》

这些数据经过整理和抽象，用于模拟不同气象条件下果园病虫害的发生情况。

## 注意事项
- 确保 `data/pest_conditions.json` 文件存在，否则程序会抛出 `FileNotFoundError` 异常。
- 配置文件路径默认值为 `config/config.json`，若使用自定义路径，请确保路径有效。
- 生成的数据集文件 `orchard_pest_disease_dataset.csv` 会覆盖之前生成的同名文件。

## 贡献
如果你对本项目有任何建议或改进意见，欢迎提交 Issue 或 Pull Request。

## 许可证
本项目采用 `BSD - 2 - Clause` 许可证。以下是许可证的详细内容：

```plaintext
BSD 2-Clause License

Copyright (c) 2025, kailynwu
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
``` 