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
