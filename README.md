# Bench

Benchmark client using [Locust](https://locust.io/).

## Usage

```bash
locust [--no-web] [-c 10] [-r 1000] [-t 10s] [--only-summary] [--logfile /dev/null] [2>err.log]
```

where:

- `--no-web` 不启动图形界面，否则需要使用 web 操作
- `-c` 设置模拟客户端数量
- `-r` 设置客户端孵化速率(每秒)
- `-t` 持续时间，默认无限长
- `--only-summary` 只有退出时显示统计数据，否则默认每 2s 刷新一次
- `--logfile` 设置日志文件，默认标准输出
- `2>...` 统计数据默认发送至标准错误

