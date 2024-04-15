import importlib
import os

from flask import Blueprint


def register_blueprints(app, package_name, package_path):
    """
    自动注册蓝图
    :param app: Flask 应用实例
    :param package_name: 包名
    :param package_path: 包路径
    """
    for root, dirs, files in os.walk(package_path):
        for filename in files:
            # 找到 Python 源文件
            if filename.endswith('.py') and not filename.startswith('__'):
                # 计算模块路径
                module_name = os.path.splitext(filename)[0]
                module_path = os.path.join(root, filename)
                # 使用 importlib 导入模块
                spec = importlib.util.spec_from_file_location(f'{package_name}.{module_name}', module_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                # 遍历模块成员
                for attribute_name in dir(module):
                    attribute = getattr(module, attribute_name)
                    # 如果是蓝图，则注册
                    if isinstance(attribute, Blueprint):
                        app.register_blueprint(attribute)
