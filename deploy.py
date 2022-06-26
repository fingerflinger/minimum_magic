import scrython
import os

asset_path = "assets"

def main():
    # Let's download some card images and put them into an assets dir
    # If folder exists
    if os.path.isfile(asset_path):
        pass
    # else, make the folder
    else:
        import pdb;pdb.set_trace()
        os.mkdir(asset_path)
    
    # For each file on list, check for exsistence. If not present, then download.
    # After downloading or if exsists already, compare hash


def download_card():
    pass
def snapshot():
    # hash the existing files for later comparison
    pass

if __name__ == "__main__":
    main()

