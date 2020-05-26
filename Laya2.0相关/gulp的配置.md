# gulp自动化任务
## 快速构建
首先检查node、npx和npm是否正确安装
```sh
node --version
npm --version
npx --version
```
没装的自己百度装一下，最好是node10.x版本，不要太高，我用的是10.18.1

安装gulp命令行工具
```sh
npm install --global gulp-cli
```
进入开发目录中
```sh
cd my-project
```
创建package.json文件
```sh
npm init
# 上述命令将指引你设置项目名、版本、描述信息等。
```
安装3.9.1版本的gulp(Laya2.0使用的是3.9.1的)
```sh
npm install --save-dev gulp@3.9.1
```
检查gulp版本
```sh
gulp --version
```

## 创建gulpfile文件
在根目录下创建一个gulpfile.js，输入：
```js
function defaultTask(cb) {
  // place code for your default task here
  cb();
}

exports.default = defaultTask
```

在项目根目录下执行 gulp 命令：
```
gulp
```
可以看到如下输出
```sh
[17:49:06] Using gulpfile ./my-project/gulpfile.js
[17:49:07] Starting 'default'...
[17:49:07] Finished 'default' after 77 μs
```
默认任务（task）将执行，因为任务为空，因此没有实际动作。