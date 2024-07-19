from requests import get as req_get

from pdb import set_trace

def search(
    q: str,
    pn: int = 1,
    ho: str = "t",
    include_ft_matches: str = "f",
    locale: str = "jp",
):
    url = f"https://sit.summon.serialssolutions.com/api/search?screen_res=W1280H348&__refererURL=&pn={pn}&ho={ho}&include.ft.matches={include_ft_matches}&l={locale}&q={q}"

    data = req_get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0" }).json()["documents"]
    return data
