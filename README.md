# Redis 

## Config Setting
* Config 전체 조회
 ```
redis> config get *
rdbchecksum
yes
daemonize
no
io-threads-do-reads
no
lua-replicate-commands
yes
always-show-logo
no
protected-mode
yes
rdbcompression
yes
rdb-del-sync-files
no
activerehashing
yes
stop-writes-on-bgsave-error
yes
set-proc-title
yes
dynamic-hz
yes
lazyfree-lazy-eviction
no
lazyfree-lazy-expire
no
lazyfree-lazy-server-del
no
lazyfree-lazy-user-del
no
lazyfree-lazy-user-flush
no
repl-disable-tcp-nodelay
no
repl-diskless-sync
no
gopher-enabled
no
aof-rewrite-incremental-fsync
yes
no-appendfsync-on-rewrite
no
cluster-require-full-coverage
yes
rdb-save-incremental-fsync
yes
aof-load-truncated
yes
aof-use-rdb-preamble
yes
cluster-replica-no-failover
no
cluster-slave-no-failover
no
replica-lazy-flush
no
slave-lazy-flush
no
replica-serve-stale-data
yes
slave-serve-stale-data
yes
replica-read-only
yes
slave-read-only
yes
...
...
save
3600 1 300 100 60 10000
client-output-buffer-limit
normal 0 0 0 slave 268435456 67108864 60 pubsub 33554432 8388608 60
unixsocketperm
0
slaveof

notify-keyspace-events

bind

oom-score-adj-values
0 200 800
```
* config 특정 항목 조회 (notify keyspace event) - 미설정된 상태
```
redis> config get notify-keyspace-events
0
notify-keyspace-events
1
```
* config Setting
 1. key event 설정
```
redis> config set notify-keyspace-events KEA
OK
```
 2. 설정된 상태 확인
```
redis> config get notify-keyspace-events
0
notify-keyspace-events
1
AKE
```
 3. 설정내용
   1. keyspace에 관한 설정은 K<br>
   2. keyevent에 관한 설정은 E<br>
   3. 그 뒤의 옵션으로 g, $, l, s, h, z, x, e등이 있으며 A를 통하여 앞의 모든것들 설정가능

