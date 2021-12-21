[TOC]

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

# 文件改动

3. 增加/删除文件
    添加指定文件到暂存区  
    $ git add [file1] [file2] ...

    添加指定目录到暂存区，包括子目录：

    ```sh
    git add [dir]
    ```

    添加当前目录下的所有文件到暂存区：

    ```sh
    git add .
    ```

4. 代码提交  
    提交暂存区到仓库区  
    $ git commit -m [message]    
    提交时显示所有diff信息  
    $ git commit -v

# 分支管理
列出所有本地分支
```sh
  git branch
```

 删除本地分支：

  ```shell
  git branch -d  local_branch_name
  ```
  创建本地分支
  `git checkout -b dev`新建并切换到本地dev分支

查看远程仓库的分支

```sh
git branch -r
```

`git merge branch_name`命令用于合并指定分支到**当前**分支

当Git无法自动合并分支时，就必须首先解决冲突。解决冲突后，再提交，合并完成。


1. 标签
    列出所有tag  
    $ git tag  
    查看tag信息  
    $ git show [tag]

2. 查看信息  
    显示有变更的文件  
    $ git status
    显示当前分支的版本历史  
    $ git log
    显示commit历史，以及每次commit发生变更的文件
    $ git log --stat

3. 远程同步

    要关联一个远程库，使用命令`git remote add origin git@server-name:path/repo-name.git`；

    关联一个远程库时必须给远程库指定一个名字，`origin`是默认习惯命名；

    显示所有远程仓库  
    $ git remote -v

4. 撤销
    恢复暂存区的指定文件到工作区  
    $ git checkout -- file_name

5. git rebase
    过多的commit会影响code review，造成分支污染
* 场景
1. 合并多次提交纪录：
    每一次功能开发， 对多个 commit 进行合并处理   

2. 分支合并

当2个分支的md5值一样的时候,`git check`就会带着你的修改去宁外一个分支

   如何解决

   - 两种方式二选一

   1. 可以使用`git stash`把工作区空间的修改隐藏起来,就可以切换到其他分支了,然后使用`git stash list`查看stash，再用`git stash pop stash@{0}`应用并删除该stash@{0}
   2. 使用`git commit`提交

版本回退

```sh
git reset --hard HEAD^   # 回退到上个版本
```

- 穿梭前，用`git log`可以查看提交历史，以便确定要回退到哪个版本。
- 要重返未来，用`git reflog`查看命令历史，以便确定要回到未来的哪个版本。
