#抓包工具tcpdump
/data/local/tmp/tcpdump --version   #同win一样，如果没加环境变量，需要跟上文件路径
#查看tcpdump版本号
#可以先
cd /data/local/tmp
./tcpdump --version  #./当前目录
./tcpdump -i any -p -s 0 -w /sdcard/capture.pcap 
# "-i any": listen on any network interface

　　# "-p": disable promiscuous(混杂） mode (doesn't work anyway)

　　# "-s 0": capture the entire packet

　　# "-w": write packets to a file (rather than printing to stdout)

　　... do whatever you want to capture, then ^C to stop it ...
#用wireshark打开即可看到数据包的详细信息。
