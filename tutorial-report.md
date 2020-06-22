# GopLE Tutorial

## 安装

```bash
sudo apt install python3-venv

# set up a virtual environment for GopLE
# 注意：文件将在当前路径创建
python3 -m venv venv-gople

# Join the environment
source venv-gople/bin/activate
# 如果没有找到 bin 目录可以用 apt 安装 virtualenv

sudo apt update

pip install git+https://github.com/django-nonrel/django@nonrel-1.5
pip install git+https://github.com/django-nonrel/djangotoolbox
pip install git+https://github.com/django-nonrel/mongodb-engine

python3 -m pip install django
```