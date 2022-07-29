# redis  보안

1. ACL

ACL(Access Control List/접근 제어)은 사용자 관리 명령입니다. 사용자를 만들고 암호(password)를 지정하고 실행 가능한 명령을 지정할 수 있습니다.

ACL로 새로운 사용자 생성 가능(password 설정)

ACL로 default 사용자에 암호 생성
```
redis> acl list
0 user default on nopass ~* &* +@all
redis> acl setuser user on >password allkeys allcommands
OK
redis> acl list
0 user default on nopass ~* &* +@all
1 user user on #5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8 ~* resetchannels +@all
redis> acl setuser default on >password
OK
redis> acl list
0 user default on #5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8 ~* &* +@all
1 user user on #5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8 ~* resetchannels +@all
```
2. Rename-Command

redis.conf에서 설정 가능

자주 쓰는 명령 및 위험한 명령어들을 다른 명령어로 대치

```
rename-command FLUSHDB a1
rename-command FLUSHALL a2
rename-command KEYS a3
rename-command DEBUG a4
rename-command SAVE a5
rename-command SCAN a6
rename-command GET a7
rename-command CONFIG a8
```

명령어 자체를 막을려면 뒤에 항목을 ""로 설정

위 명령어 변경을 통하면 python redis함수 재정의 필요

3. PythonScript로 Redis.conf 암복호화
```
def encrypt_file(filename):
    with open(filename, 'r') as f:
        data = f.read()
    with open(filename, 'w') as f:
        data1 = 암호화
        f.write(data1)

def decrypt_file(filename):
    with open(filename, 'r') as f:
        data = f.read()
    with open(filename, 'w') as f:
        data1 = 복호화
        f.write(data1)

if len(sys.argv) == 2:
    import time
    os.system("redis-cli shutdown")	#기존 실행되는 redis-server종료
    decrypt_file(sys.argv[1])	#config 파일 복호화
    os.system("redis-server redis.conf &")	#background로 redis-server 실행(복호화된 config파일)
    time.sleep(1)	#잠시 대기 후
    encrypt_file(sys.argv[1]) #config 파일 암호화
# elif len(sys.argv) == 3:
#    if int(sys.argv[2]) == 1:
#        encrypt_file(sys.argv[1])
#    else:
#        decrypt_file(sys.argv[1])
```
