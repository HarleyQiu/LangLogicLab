from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/get_company_info', methods=['GET'])
def get_company_info():
    data = {
        "company_details": {
            "demand_name": "示例需求",
            "company_name": "示例公司",
            "industry": "IT",
            "budget_amount": 100,
            "delivery_time": "2023-12-31",
            "delivery_requirements": "详细规范和文档",
            "work_frequency": "每周五次",
            "transaction_duration": "2小时",
            "average_workload": "中等",
            "labor_cost": 50000,
            "number_of_employees": 10,
            "contact_person": "张三",
            "contact_info": "zhangsan@example.com"
        },
        "dialogues": [
            {"question": "能否介绍一下您的需求名称及所在公司和行业？",
             "answer": "当然，我们的需求名称是“示例需求”，我们的公司名为“示例公司”，主要从事 IT 行业。"},
            {"question": "您的项目预算是多少，以及您希望的交付时间是什么时候？",
             "answer": "我们的项目预算大约是100万元。我们希望能够在2023年12月31日前完成交付。"},
            {"question": "您能详细描述一下交付要求吗？",
             "answer": "当然，我们的交付要求包括提交一份详细的规范和文档，确保项目符合我们的标准。"},
            {"question": "您的工作频率和单笔业务处理时间是怎样的？",
             "answer": "我们的工作频率是每周五次，而每笔业务的处理时间大约需要2小时。"},
            {"question": "您的平均工作量、人工成本和员工数分别是多少？",
             "answer": "我们的平均工作量是中等水平，人工成本大约是50000元，目前公司的员工数是10人。"},
            {"question": "我可以联系谁来了解更多信息？他们的联系方式是什么？",
             "answer": "您可以联系我们的负责人张三。他的联系方式是 zhangsan@example.com。"},
        ]
    }
    return jsonify(data)


@app.route('/get_pricing_info1', methods=['GET'])
def get_pricing_info1():
    pricing_info = {
        "title": "GitHub Copilot",
        "product_description": "GitHub Copilot 是由 GitHub 和 OpenAI 共同开发的一款人工智能编程助手。它通过理解你的代码及其上下文，自动提供代码建议和补全功能。",
        "pricing": {
            "individual_users": {
                "description": "个人用户套餐",
                "price": "10美元",
                "billing_cycle": "每月",
                "features": "为个人开发者提供全功能访问权限"
            },
            "enterprise_users": {
                "description": "企业用户套餐",
                "price": "19美元",
                "billing_cycle": "每个用户/月",
                "features": "为企业级用户提供额外的协作和管理功能"
            }
        }
    }
    return jsonify(pricing_info)


@app.route('/get_pricing_info2', methods=['GET'])
def get_pricing_info2():
    pricing_info = {
        "title": "GitHub Copilot",
        "product_description": "GitHub Copilot 是由 GitHub 和 OpenAI 共同开发的一款人工智能编程助手。它通过理解你的代码及其上下文，自动提供代码建议和补全功能。",
        "pricing": "GitHub Copilot 的个人用户套餐每月10美元，提供全功能访问权限；而企业用户套餐则为每个用户每月19美元，专为企业级用户提供额外的协作和管理功能。"
    }
    return jsonify(pricing_info)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8555, debug=True)
