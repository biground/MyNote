# CentOS/Ubuntu下安装

## 安装依赖包
+ CentOS:
```
yum -y install git gcc make patch zlib-devel gdbm-devel openssl-devel sqlite-devel bzip2-devel readline-devel
```
+ Ubuntu:
```
apt-get -y install git gcc make patch zlib1g.dev libgdbm-dev libssl-dev libsqlite3-dev libbz2-dev libreadline-dev
```
## 安装pyenv
1. 安装
```
curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | zsh
```
2. 设置环境变量
```
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.zshrc
exec "$SHELL"
```

# pyenv使用指南
1. pyenv version 查看系统安装的python版本
2. pyenv install \<versions\> 安装其他版本python
3. pyenv local \<versions\> 切换python版本

# pyenv-virtualenv使用指南
1. pyenv virtualenv \<versions\> \<virtualenv-name\> 创建虚拟环境
```
pyenv virtualenv 3.6.0 venv-3.6.0
```
2. 创建项目，让项目使用干净的python3.6.0虚拟环境
```
mkdir myproject
cd myproject
pyenv local venv-3.6.0
pyenv activate venv-3.6.0
```