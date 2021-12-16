git  
是一个分布式版本控制软件  
1. 新建代码库  
在当前目录新建一个Git代码库  
$ git init

新建一个目录，将其初始化为Git代码库  
$ git init [project-name]  

下载一个项目和它的整个代码历史  
$ git clone [url]  

2. 配置  
  显示当前git配置  
  git config --list  

3. 增加/删除文件
  添加指定文件到暂存区  
  $ git add [file1] [file2] ...

4. 代码提交  
  提交暂存区到仓库区  
  $ git commit -m [message]    
  提交时显示所有diff信息  
  $ git commit -v

5. 分支
  列出所有本地分支  
  `git branch`

  在 Git 中删除本地分支的命令是：

  ```shell
  git branch -d  local_branch_name
  ```

    创建本地分支

  `git checkout -b dev`新建并切换到本地dev分支

6. 标签
  列出所有tag  
  $ git tag  
  查看tag信息  
  $ git show [tag]

7. 查看信息  
  显示有变更的文件  
  $ git status
  显示当前分支的版本历史  
  $ git log
  显示commit历史，以及每次commit发生变更的文件
  $ git log --stat

8. 远程同步
  显示所有远程仓库  
  $ git remote -v

9. 撤销
  恢复暂存区的指定文件到工作区  
  $ git checkout [file]

10. git rebase
    过多的commit会影响code review，造成分支污染
* 场景
1. 合并多次提交纪录：
每一次功能开发， 对多个 commit 进行合并处理   
2. 分支合并

