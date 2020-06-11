# GopLE Tutorial

## Django/MongoDB 安装

```bash
pip install virtualenv
# sudo apt instal virtualenv

# set up a virtual environment for GopLE
# 注意：文件将在当前路径创建
virtualenv --no-site-packages venv-gople

# Join the environment
source venv-gople/bin/activate
# 如果没有找到 bin 目录可以用 apt 安装 virtualenv

pip install git+https://github.com/django-nonrel/django@nonrel-1.5
pip install git+https://github.com/django-nonrel/djangotoolbox
pip install git+https://github.com/django-nonrel/mongodb-engine
```