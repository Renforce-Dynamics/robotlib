import os

def config_dir(*args):
    dir = os.path.join(*args)
    os.makedirs(dir, exist_ok=True)
    return dir

ROBOTLIB_REPO_DIR                 = os.path.dirname(os.path.abspath(__file__))
ROBOTLIB_DATA_DIR                 = os.path.join(ROBOTLIB_REPO_DIR, "..", "..", "..", "data")

ROBOTLIB_ASSETS_DIR               = os.path.join(ROBOTLIB_DATA_DIR, "assets")
ROBOTLIB_USD_DIR                  = os.path.join(ROBOTLIB_ASSETS_DIR, "usd")

ROBOTLIB_ASSETLIB_DIR             = os.path.join(ROBOTLIB_ASSETS_DIR, "assetslib")