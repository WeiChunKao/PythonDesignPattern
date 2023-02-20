import requests
from threading import Thread


class DownloadThread(Thread):
    CHUNK_SIZE = 1024 * 512

    def __init__(self, fileName, url, savePath, callBackProgress, callBackFinished):
        super().__init__()
        self._fileName = fileName
        self._url = url
        self._savePath = savePath
        self._callBackProgress = callBackProgress
        self._callBackFinished = callBackFinished

    def run(self):
        readSize = 0
        r = requests.get(self._url, stream=True)
        totalSize = int(r.headers.get('Content-Length'))
        with open(self._savePath, 'wb') as file:
            for chunk in r.iter_content(chunk_size=self.CHUNK_SIZE):
                if chunk:
                    file.write(chunk)
                    readSize += self.CHUNK_SIZE
                    self._callBackProgress(self._fileName, readSize, totalSize)
        self._callBackFinished(self._fileName)


def testDownload():
    def downloadProgress(fileName, readSize, totalSize):
        percent = (readSize / totalSize) * 100
        print(f"[Download {fileName}] Progress:{percent}")

    def downloadFinished(fileName):
        print(f"[Download {fileName}] Finished")
    print(f"Download Lena")
    downloadUrl1 = "http://www.lenna.org/full/l_hires.jpg"
    download1 = DownloadThread(
        "testDownload", downloadUrl1, './lena.png', downloadProgress, downloadFinished)
    download1.start()


if __name__ == "__main__":
    testDownload()
