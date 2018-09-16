#!/bin/bash
PROJ=map
while getopts "rk" arg #选项后面的冒号表示该选项需要参数
do
        case $arg in
             r)
               mux start $PROJ
                ;;
             k)
                tmux kill-session -t $PROJ
                ;;
             ?)  #当有不认识的选项的时候arg为?
            echo "Usage:"
            echo "./box.sh -r   --- 启动"
            echo "./box.sh -k   --- 杀死" 
        exit 1
        ;;
        esac
done

