from google_images_search import GoogleImagesSearch
from dotenv import load_dotenv
import os`

load_dotenv()
GCS_DEVELOPER_KEY = os.environ.get("GCS_DEVELOPER_KEY")
GCS_CX = os.environ.get("GCS_CX")

gis = GoogleImagesSearch(GCS_DEVELOPER_KEY, GCS_CX)

_search_params = {
    'q': 'basketball court',
    'num': 10,
    'fileType': 'jpg',
    'rights': 'cc_publicdomain'
}

gis.search(search_params=_search_params, path_to_dir='images')
