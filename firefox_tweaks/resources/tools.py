import os
import glob
import platform


def get_firefox_profile_path() -> str:
    """Detects Firefox's profiles path based on the recognized OS.

    Raises:
        OSError: Raised when the script cannot be executed in the user's OS.

    Returns:
        str: The path to the profiles storage.
    """
    system = platform.system()

    if system == "Windows":
        app_data = os.getenv("APPDATA")
        return os.path.join(app_data, "Mozilla", "Firefox", "Profiles")
    
    elif system == "Linux":
        return os.path.expanduser("~/.mozilla/firefox/")
    
    elif system == "Darwin":  # macOS (why the heck is it called Darwin?)
        return os.path.expanduser("~/Library/Application Support/Firefox/Profiles/")
    
    else:
        raise OSError("❌ Unsupported OS")
    

def get_default_profile() -> list[str]:
    """Selects Firefox's default profile.

    Raises:
        FileNotFoundError: Raised when the script were unable to detect any Firefox's profiles.

    Returns:
        profiles (list[str]): The default profile defined in Firefox (first element of the list).
    """
    profile_dir = get_firefox_profile_path()
    profiles = glob.glob(os.path.join(profile_dir, "*.default*"))

    if not profiles:
        raise FileNotFoundError("❌ No Firefox profile was found!")
    return profiles[0]


def already_installed(PROFILE_PATH: str, extension_id: str) -> bool:
    """Checks if an extension is already installed in the Firefox profile.

    Args:
        PROFILE_PATH (str): The location for the default Firefox profile where the changes will be applied.
        extension_id (str): _description_

    Returns:
        bool: _description_
    """
    extensions_dir = os.path.join(PROFILE_PATH, "extensions")
    return os.path.exists(os.path.join(extensions_dir, f"{extension_id}.xpi"))