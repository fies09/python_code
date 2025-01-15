#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time       : 2023/7/9 16:12
# @Author     : fany
# @Project    : PyCharm
# @File       : auto_installpackages.py
# @description:
import subprocess
import os
import time
import pkg_resources
file_name = 'requirements.txt'



def get_package_versions():
    installed_packages = pkg_resources.working_set
    package_versions = []
    for package in installed_packages:
        package_name = package.project_name
        package_version = package.version
        package_versions.append(f"{package_name}=={package_version}")
    return package_versions

def generate_requirements_file(filen_name=file_name):
    package_versions = get_package_versions()
    with open(filen_name, 'w') as file:
        file.write('\n'.join(package_versions))


def check_installed_packages(package_list):
    installed_packages = set()
    with subprocess.Popen(['pip', 'freeze'], stdout=subprocess.PIPE, universal_newlines=True) as proc:
        for line in proc.stdout:
            package_name = line.split('==')[0].strip()
            installed_packages.add(package_name)

    missing_packages = package_list - installed_packages

    if missing_packages:
        print("Missing packages: ", missing_packages)
        install_packages(missing_packages)
        update_requirements(missing_packages)
    else:
        print("All packages are already installed.")

def install_packages(packages):
    for package in packages:
        try:
            subprocess.check_call(['pip', 'install', '--upgrade', package])
            print(f"Successfully installed/updated package: {package}")
        except subprocess.CalledProcessError as e:
            print(f"Failed to install/update package: {package}")

def update_requirements(packages):
    with open(file_name, 'a+') as file:
        file.seek(0)
        installed_packages = set(line.strip() for line in file)
        missing_packages = packages - installed_packages

        if missing_packages:
            file.write('\n')
            file.write('\n'.join(missing_packages))
            print("Updated requirements.txt file.")
        else:
            print("All packages are already listed in requirements.txt.")

if __name__ == "__main__":
    if not os.path.exists('./' + file_name):
        generate_requirements_file()
    # 读取requirements.txt文件中的包列表
    with open(file_name, 'r') as file:
        requirements = set(line.strip() for line in file)
    # 检查已安装的包是否在requirements.txt文件中
    check_installed_packages(requirements)
    # 检查并更新pip
    try:
        subprocess.check_call(['pip', 'install', '--upgrade', 'pip'])
        print("Successfully updated pip.")
    except subprocess.CalledProcessError as e:
        print("Failed to update pip.")
