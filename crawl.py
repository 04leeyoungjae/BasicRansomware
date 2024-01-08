import os
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

if __name__=="__main__":
    if not os.path.exists("C:\\test"):
        os.makedirs("C:\\test", exist_ok=True)
    files=search_file("C:\\program files",".png",".jpg",".txt")
    for file in files:
        with open(file,"rb") as source:
            with open("C:\\test\\"+os.path.basename(file),"wb") as dest:
                dest.write(source.read())