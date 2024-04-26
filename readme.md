# 电玩猩店铺数据分析报告生成
该代码用于生成电玩猩店铺数据分析报告的自动化工具。它可以根据输入的店铺名称、日期范围等参数，从数据库中提取数据并生成相应的报告。

1. **安装环境**

确保已安装所需的Python依赖项。具体环境在：requirements.txt

2. **数据库配置**

auto_generate_test.py代码的auto_generepot()中配置，db_info

3. **运行代码并生成HTML**

auto_generate_test.py的generate()函数即可生成报告。可在代码中调整输入参数以生成不同的报告。

4. **代码结构**

* auto_content_test.py: 包含报告的目录模板，例如主观问题等。
* **auto_generate_test**.py: 主函数，包括详细的子问题目录，调用文心一言，生成报告
* db_dwx: 存放与电玩猩店铺数据相关的数据库操作工具。
* Fun_LLM: 存放gpt,文心一言相关的代码。
* report_3.html: 报告模板文件，用于渲染生成最终的HTML报告。

5. **auto_generate_test 详细说明**

* auto_generepot主要函数，：子问题构建：结果存在all_report_question
* 主观问题，即需要调用gpt的问题，在注释中有标注，目前使用的是文心一言，之后可以更换接口。
* 整个报告的主观问题描述存在chat_question，可用来生成优化策略
* 剩余待办：注释里 TODO，主要是更改接口和整体优化策略的生成

6. 报告结果
在output_dwx_test.html中查看生成的报告示例。