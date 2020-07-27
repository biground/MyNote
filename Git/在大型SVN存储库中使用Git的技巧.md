# 在大型Subversion存储库中使用Git的实用技巧
在使用Git作为Svn客户端之前，先说明几点警告：
1. 跟踪所有的svn分支和标签是不切实际的。最好只跟踪主干和一些选定的分支
2. 初始clone会花费很长时间，可能会被中断，需要几次手动的恢复
3. 对于主干的克隆可能会完全崩溃，并且根本无法正常工作。这种情况很少发生，但如果发生了，那么就将无法使用Svn。
4. 如果在项目中混合了LF和CRLF，则行尾字符可能会出现问题。潜在问题不可忽略，例如，可能无法查看非常规注释。但是，这是可以并且应该在项目中解决的问题。
5. 克隆时必须使用命令行

## 创建本地仓库
首先，在本地创建一个空白文件夹src，然后终端进入到src
```sh
mkdir src
cd src
```
如果已安装git-svn，使用git svn init svnpath 来创建本地的Git仓库
```sh
git svn init svn://username@host/filepath
```
然后使用git svn fetch克隆一个版本的源码
```sh
git svn fetch -r 6666:HEAD
```

不要克隆整个Svn存储库。因为会耗费很久的时间，而且文件夹会变得异常庞大。

如果存储库足够大，则克隆可能会中断。这时src目录中会包含.git子目录。进入src目录并继续执行以下操作：

`git svn fetch`

根据存储库的大小，您可能必须重复几次，直到克隆完成。
当克隆完成时，要生成一个基于svn的元数据的gitignore文件：

`git svn show-ignore >> .gitignore`

从Svn克隆完成后，便有了一个Git存储库。

然而，为了保持环境整洁并避免影响同事，最好使master保持在最后一次rebase的状态，即永远不要在master上进行任何工作，仅将master分支用于与远程Svn存储库进行交互，例如请求更新和推送本地事务，而工作必须在本地分支上进行。

## 将其添加到Sourcetree中
打开Sourcetree，新建->添加已经存在的本地仓库，添加src文件夹即可

## 获取更新

使用`git svn rebase`获取svn存储库的最新版本

## 提交到svn

假设您修复了一个名为bug123的分支上的错误，并且从未接触过master。您有两个主要选择：
+ 在bug123中保留您的个人提交
+ 将您的个人提交压缩到bug123中，然后在一次提交中应用更改

## 将分支上的提交合并到master上
由于Svn不像Git那样具有分支的概念，因此保留单个提交的最简单方法是将分支rebase到Svn的主干（= master），然后将提交推送到Svn：
```sh
git checkout master # 先更新远端的最新版本
git svn rebase
git checkout bug123 # 接下来，将bug123分支rebase到主干上
git rebase master
git checkout master
git merge bug123 # 这应该是一个fast-forward
git svn dcommit
```

## 将分支上的提交合并为一个提交
```sh
git checkout master
git svn rebase
git merge bug123
git svn dcommit
```
