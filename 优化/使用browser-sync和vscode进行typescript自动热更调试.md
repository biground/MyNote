### 起因
Laya IDE中的Debug使用的是`tsc -p . --outDir bin/js`命令将src/modules中的.ts文件编译并输出到对应的bin/js目录下，虽然按个F5就能启动调试，但是不管你更改了多少内容，每次调试都要等30-60秒左右浏览器才会启动。

### layaair-cmd 介绍
layaair-cmd是layaair的命令行工具，使用layaair-cmd可以在不打开IDE的情况下对layaair项目进行编译发布的操作，经常使用的功能有：  
功能|子命令
-|-
编译|compile
导出UI|ui
打开静态文件服务器|open
#### 安装
`$npm install layaair-cmd -g`  
#### CLI
1. 编译项目  
`layaair-cmd compile`
2. 导出UI（仅代码）  
`layaair-cmd ui -c -d`

[layaair-cmd文档](http://npm.taobao.org/package/layaair-cmd)

### browser-sync 介绍
Browsersync能让浏览器实时响应文件的更改(html,js,css等)并自动刷新页面
#### 安装
`npm insatll browser-sync -g`
#### 启动
`browser-sync start --server --files "**/*.js" // 监听所有目录下js文件的更改`  
[browser-sync文档](https://www.browsersync.io/docs)

### launch.json 介绍
在vscode中调试Chrome应用，首先添加Debugger for Chrome
,接着要创建运行配置文件launch.json。在LayaIDE中，默认的调试行为是launch，在项目中的.laya文件夹下可以看到有个chrome的目录，它会打开启动这个目录下的chrome应用程序进行调试。  
本文介绍的热更调试方法需要在使用browser-sync启动小型服务器并在打开chrome后再启动vscode中的附加(attach)调试。其中port和url参数中的端口是可以自定义的，这里使用的都是默认端口。
```json
{
	"version": "0.2.0",
	"configurations": [
		{
			"name": "chrome调试",
			"type": "chrome",
			"request": "attach",
			"port": 9222,
			"url":"http://localhost:3010/bin",
			"sourceMaps": true,
			"webRoot": "${workspaceRoot}/bin"
		}
	]
}
```

### tsc.py
这是我结合layaair-cmd写的一个编译脚本，支持以下几个编译命令
1. 按`tsc -p . --outDir bin/js`进行整个项目的编译  
`python -m tsc --outDir`
2. 按`layaair-cmd ui -c -d`进行ui文件的导出  
`python -m tsc --ui`
3. 按`tsc --outFile ${outputPath} --target es5 --module commonjs --sourceMap true ${inputPath}`进行单个文件（更改过的文件）的编译  
`python -m tsc --outFiles`

在每次进行`python -m tsc --outFiles`的操作时，程序会维护一个mFiles.json的文件，这个json文件保存了src/modules目录下每个文件的md5值，当脚本运行时，程序就会检测目录下所有文件的md5值，当检测到文件的md5值变化时，就说明这个文件被更改了，这个文件的路径就会保存到sourceList中并生成一个对应bin/js的路径保存到outputList中。当遍历结束时，就会对列表中的每个文件进行`tsc --outFile`编译生成对应的js和js.map文件。

### 配置
1. 首先安装好visual studio code、layaair-cmd和browser-sync
2. 在visual studio code中安装好Debugger for Chrome的扩展
3. ctrl+p打开launch.json文件，将这段配置复制进去，保存关闭
```json
{
	"version": "0.2.0",
	"configurations": [
		{
			"name": "chrome调试",
			"type": "chrome",
			"request": "attach",
			"port": 9222,
			"url":"http://localhost:3010/bin",
			"sourceMaps": true,
			"webRoot": "${workspaceRoot}/bin"
		}
	]
}
```
4. 打开命令行，切换到工作目录，在命令行中输入下面的命令启动browser-sync  
`browser-sync start --server --files "**/*.js" --browser chrome --startPath bin --port 3010`  
通过命令行启动chrome并打开vscode中对应的端口  
`'/c/Program Files (x86)/Google/Chrome/Application/chrome.exe' --remote-debugging-port=9222`  
然后在地址栏中输入`http://localhost:3010/bin/`打开游戏
5. 在vscode中按下f5启动调试，就会自动attach到Chrome中进行调试了
6. 每次更改了ts文件后，只要在命令行中输入`python -m tsc --outFiles`或者`python -m tsc --ui`就会只对更改过的文件或是ui文件进行编译输出，输出js或者ui文件后，browser-sync就会自动进行刷新操作，这样就不用重新启动chrome就能热更调试了！
> 因为没有深入研究layaair-cmd这个工具，对于一些比较奇怪的问题，或是添加了ui或是ts文件，或是要导出合图，或是除了ts文件的更改，还是建议打开Laya的IDE进行编译或导出。这个方法目前还只是比较使用小范围更改的调试。

### 性能比较
举个例子：
在只添加了一行代码的情况下编译或是调整了ui中一个像素后导出ui的情况下：  
| |使用tsc脚本|不使用tsc脚本|
|-|-|-|
|导出UI|6秒|1分14秒|
|编译运行|2秒|57秒|
在更改了大量代码的情况下编译或是调整许多ui文件后导出ui还是建议使用LayaIDE进行编译和导出

> 注：如果Chrome是你的默认浏览器，这种方式会使得windows其他应用不能用系统默认浏览器打开Chrome，可以考虑使用火狐（这不是广告）