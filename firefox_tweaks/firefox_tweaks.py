import json
import os
import requests
from resources.tools import (get_default_profile, already_installed)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROFILE_PATH = get_default_profile()

def setup_user_js(PROFILE_PATH: str) -> None:
    """Reads and applies 'user.js' to Firefox (about:config custom settings).

    Args:
        PROFILE_PATH (str): The location for the default Firefox profile where the changes will be applied.

    Raises:
        FileNotFoundError: Raised when the script were unable to detect the custom configuration file.
    """
    custom_user_js = os.path.join(SCRIPT_DIR, "resources", "user.js")
    if not os.path.exists(custom_user_js):
        raise FileNotFoundError(f"❌ '{custom_user_js}' not found in the script directory!")

    with open(custom_user_js, "r") as f:
        custom_user_js_content = f.read()

    user_js_path = os.path.join(PROFILE_PATH, "user.js")
    with open(user_js_path, "w") as f:
        f.write(custom_user_js_content)
    print(f"✅ 'user.js' was applied to: '{user_js_path}'")


def install_extensions(PROFILE_PATH: str) -> None:
    """Installs the extensions defined in 'extensions.json'

    Args:
        PROFILE_PATH (str): The location for the default Firefox profile where the changes will be applied.
    """
    extensions_file = os.path.join(SCRIPT_DIR, "resources", "extensions.json")
    extensions_dir = os.path.join(PROFILE_PATH, "extensions")
    os.makedirs(extensions_dir, exist_ok=True)
    
    with open(extensions_file, "r") as f:
        ext_to_install = json.load(f)

    for ext_name, ext_url in ext_to_install.items():
        ext_id = ext_name
        ext_path = os.path.join(extensions_dir, f"{ext_id}.xpi")
        
        if already_installed(PROFILE_PATH, ext_id):
            print(f"⏩ '{ext_name}' is already installed. Skipping...")
            continue
           
        print(f"⬇️ Downloading '{ext_name}'...")
        try:
            response = requests.get(ext_url)
            response.raise_for_status()
            with open(ext_path, "wb") as f:
                f.write(response.content)
            print(f"✅ Installed '{ext_name}'")
        except Exception as e:
            print(f"❌ Failed to install '{ext_name}': {e}")


if __name__ == "__main__":
    print("🔥🦊 Starting Firefox Auto-Configuration...")
    setup_user_js(PROFILE_PATH)
    install_extensions(PROFILE_PATH)
    print("🎉 Firefox setup complete! Restart Firefox for changes to apply.")