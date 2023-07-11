# 前置依赖
```
python3 -V
```
Python ≥ 3.9

**如果python不满足条件则参考**[python安装3.9](https://blog.csdn.net/qq_28770757/article/details/109684720)*.
```
openssl version
```
openssl ≥ 1.1.1
#### 如果openssl不满足条件则依次执行下面的命令
```bash
wget https://www.openssl.org/source/openssl-1.1.1i.tar.gz    # 下载openssl1.1.1
tar -xzvf openssl-1.1.1i.tar.gz -C /usr/local/               # 解压到本地路径
cd /usr/local/openssl-1.1.1i                                 # 进入openssl解压路径
./config                  # 配置openssl
make -j2 && make install  # 编译openssl并安装,-j2是加速编译,2核服务器就-j2,16核就-j16,
                          # 时间较长，取决于服务器性能
ln -sf /usr/local/lib64/libssl.so.1.1 /usr/lib64/libssl.so.1.1        # 软链,环境相关
ln -sf /usr/local/lib64/libcrypto.so.1.1 /usr/lib64/libcrypto.so.1.1  # 软链,环境相关
```
#### 新开一个终端
```bash
openssl version
```
显示openssl === 1.1.1i
## 克隆项目（建议采用）github源
```
git clone --depth=1 https://github.com/LS-plan/lzapp.git ./lzapp/
```
## 或者gitee源
```
git clone --depth=1 https://gitee.com/LS-plan/lzapp.git ./lzapp/
```
## 进入目录并安装依赖
```
cd lzapp && pip3 install -r requirements.txt
```
## 运行
```
python3 app.py
```

## 可能用到的
1. 降低urllib3版本
```
python3 -m pip install urllib3==1.26.6
```
2. 如果出现"花了太长时间进行响应"或者是"拒绝了相应"之类的
开放对应的端口5002就可以
