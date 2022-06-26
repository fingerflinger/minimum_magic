import scrython
import os

asset_path = "assets"


# Let's download some card images and put them into an assets dir
def main():
    # If folder doesn't exist
    import pdb;pdb.set_trace()
    if not os.path.exists(os.path.join(os.getcwd(), asset_path)):
        os.mkdir(asset_path)
    
    # For each file on list, check for exsistence. If not present, then download.
    # After downloading or if exsists already, compare hash

    download_card("Mountain")

def download_card(card_def):
    # TODO define card by scryfall id, but how to get the id of versions I actually want to use?
    card = scrython.cards.Named(fuzzy=card_def)

# hash the existing files for later comparison
def snapshot():
    pass

if __name__ == "__main__":
    main()

