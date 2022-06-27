import scrython
import os
import urllib.request
import hashlib

asset_path = "assets"

card_list = [("Mountain", "e1af2d09-908e-442e-a9d0-9c618a71a327")] # Mountain


def generate_manifest(card_list, asset_path):
    # TODO
    # generate a manifest that enables us to check our environment is set up correctly 
    pass

def find_card(card_name, set_code='', artist=''):
    query = "name:\"{}\"".format(card_name)
    if set_code:
        query += " set:\"{}\"".format(set_code)
    if artist:
        query += " artist:\"{}\"".format(artist)

    results = scrython.cards.Search(q=query)
    if results.total_cards() == 1:
        return results
    else:
        return False # Err code too?

def hash_file(file_loc):
    with open(file_loc, mode='rb') as my_file:
        file_contents = my_file.read()
        m = hashlib.md5()
        m.update(file_contents)
        my_hash = m.hexdigest()
        return my_hash

def check_file(file_loc):
    if(os.path.isfile(file_loc)): 
        return hash_file(file_loc)
    return False

def do_download(uri, destination, verification_hash=""):
    if(verification_hash):
        check_file(destination, verification_hash)
    urllib.request.urlretrieve(uri, destination)
    # TODO check for file

def construct_file_name(card_name, suffix):
    # TODO
    # Need to handle spaces and tricky characters in the card names
    return card_name + "_small.jpg"

def download_card(card_id, destination, verification_hash):
    card = scrython.cards.Id(id=card_id)
    my_links = card.image_uris()
   
    if ("small" in my_links.keys()):
        do_download(my_links["small"], os.path.join(destination, construct_file_name(card.name(), "_small.jpg")))
    
    if ("normal" in my_links.keys()):
        do_download(my_links["normal"], os.path.join(destination, construct_file_name(card.name(), "_normal.jpg")))

# hash the existing files for later comparison
def snapshot():
    pass

# Let's download some card images and put them into an assets dir
def main():
    # If folder doesn't exist
    if not os.path.exists(os.path.join(os.getcwd(), asset_path)):
        os.mkdir(asset_path)
    
    # For each file on list, check for exsistence. If not present, then download.
    # After downloading or if exsists already, compare hash
    download_card(card_list[0], asset_path)

if __name__ == "__main__":
    main()

