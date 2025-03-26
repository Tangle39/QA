#!/bin/bash
# 查找指定目录下的最小和最大的文件，并输出它们的名称及大小
# 检查是否传入参数
if [ -z "$1" ]; then
    echo "Usage: $0 <directory>"
    echo "Please specify a directory to analyze."
    exit 1
fi

# 获取传入的目录
dir=$1

# 检查目录是否存在
if [ ! -d "$dir" ]; then
    echo "Error: Directory '$dir' does not exist."
    exit 1
fi

# 查找目录下的所有文件
file_list=$(find "$dir" -type f)

# 检查目录是否为空
if [ -z "$file_list" ]; then
    echo "The directory '$dir' contains no files."
    exit 0
fi

# 查找最小和最大文件
find "$dir" -type f -exec du -h "{}" + | sort -h | \
awk 'NR==1{print "Min file: "$2, "Size: "$1} END{print "Max file: "$2, "Size: "$1"}'
