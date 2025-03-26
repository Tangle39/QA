# Mac命令  
打开某个隐藏文件夹：`open /usr/bin` 
寻找某个名字的文件：`sudo find / -iname ‘chromedriver'` 

## SIP

System Integrity Protection，enable将保护 /system /sbin /usr 这三个目录

查看SIP状态：`csrutil status` 

* disable

  将 Mac 开机，立即在键盘上按住 Command ⌘ + R，直到看到 Apple 标志或旋转的地球时松开。看到「实用工具」窗口时，恢复功能启动即完成。点击「实用工具」选择「终端」

  `csrutil disable`

* enable

  `csrutil enable`

防止 .DS_Store 文件的生成: defaults write com.apple.desktopservices DSDontWriteNetworkStores true 

软件有经过了汉化或者破解，所以可能被Mac认为「已损坏」
`$ sudo spctl --master-disable` 即可~

export 查看当前环境变量

* 显示隐藏文件

键盘键Cmd + Shift +.

* 查看电池情况

`ioreg -rn AppleSmartBattery | grep -i capacity`

* 从zsh切回bash

  ```sh
  chsh -s /bin/bash
  ```

* 清除小红点(临时)

  ```sh
  defaults write com.apple.systempreferences AttentionPrefBundleIDs 0
  ```

# 开机启动项

设置→用户与群组→登录项

部分软件这里找不到

在`/Library/LaunchAgents`

1. 找到对应程序的 .plist 文件
2. 删除 SuccessfulExit 属性。
3. 将 RunAtLoad / KeepAlive 均设为 <false/>

参考自: https://www.zhihu.com/question/28268529

