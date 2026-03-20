import subprocess
import datetime
import os

def push():
    status = f"--- 104核战神集群报告 ---\n时间: {datetime.datetime.now()}\n负载: {subprocess.getoutput('uptime')}\n"
    with open("cluster_status.txt", "w") as f:
        f.write(status)
    print("✅ 状态文件已生成")

if __name__ == "__main__":
    push()
