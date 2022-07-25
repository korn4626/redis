# Redis 

## Config Setting
### Config 전체 조회
<details>
  <summary>접기/펼치기</summary>
  <div markdown="1"> 
   
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
</div>
</details>

### Config 특정 항목 조회 (notify keyspace event) - 미설정된 상태
```
redis> config get notify-keyspace-events
0
notify-keyspace-events
1
```

### Config Setting
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
  - keyspace에 관한 설정은 K<br>
  - keyevent에 관한 설정은 E<br>
  - 그 뒤의 옵션으로 g, $, l, s, h, z, x, e등이 있으며 A를 통하여 앞의 모든것들 설정가능

## SourceCode
### 키생성
[MakeKey.py](https://github.com/korn4626/Redis_KeyEvent/blob/main/MakeKey.py)
* 임의의 키 생성 - 1000건을 기준으로 키를 생성하거나 삭제. 수시로 기준 항목 경계로 임의의 키 생성로직

### Notification
[subscribeKey.py](https://github.com/korn4626/Redis_KeyEvent/blob/main/subscribeKey.py)
* 0번 서버(키리스트) 항목을 notification
  * 해당 키의 dbsize를 읽어서 MaxCapacity 비교 => dbsize()함수 실행 속도 이슈로 실시간 반영 안됨. 
  * key event 확인 : set, del 이벤트는 제대로 들어오는 부분 확인하여 해당 방식으로 count
  * 기준 항목 MaxC(1000건)보다 큰 경우 TRList에 저장, 작은 경우 TRList 삭제
* subscribe, psubscribe 차이점
  * psubscribe는 pattern으로 구독!!->subscribe는 해당 키를 콕 찝어서...
 
### Notification2
[extest.py](https://github.com/korn4626/Redis_KeyEvent/blob/main/extest.py)
* curC 항목 읽어서 max 값보다 올라가면 출력
