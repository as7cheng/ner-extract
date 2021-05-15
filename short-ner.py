from spellchecker import SpellChecker
from states import us_states
from countries import country
import sys

'''
# For testing
inputs = ["payal * US NY - Doodash", "sq* NJ SEAMLSS 2017777777", "SEAMLSS MCd",
          "McDOnalds UBEREATS", "Giftcard CA US", "Hotels.com Expedia Sheraton", "Chipotl Postmates", "paypal * US - Grubhub",
          "payal * US NY - ubereats", "sq* NJ doordash 5745745745", "SEAMLSS Subway", "wendy's UBEREATS", "Giftcard TX US",
          "booking.com priceline marriott", "chickfila Postmates"]
'''

# Simple database of brands
brands = {"paypal", "doordash", "sq", "seamless", "mcdonalds", "ubereats", "giftcard", "hotels.com", "expedia",
           "sheraton", "chipotle", "postmates", "grubhub", "subway", "wendys", "booking.com",
           "priceline", "marriott", "chickfila"}
# Database for unclear input
unclear_brands = {"mcd" : "mcdonalds", "payal": "paypal", "doodash": "doordash"}

# Symbols to be ingnored
symbols = ["*", "-", "", "'"]

# Spell check tool
spell = SpellChecker()

# Function to access input, return a list contains only readable words
def access_input(input):
    input_list = input.split(" ")
    for symbol in symbols:
        try:
            input_list.remove(symbol)
        except:
            pass
    return input_list

# Function to access single strings, return a string as the word without any symbols
def access_str(s):
    for symbol in symbols:
        try:
            s = s.replace(symbol, '')
        except:
            pass
    return s

# Function to extract the entire input
def extract_input(input):
    # Get a valid list contains words
    input_list = access_input(input)
    # Create output
    output = {"brand" :[{}], "state": "", "country": "", "ph no": ""}
    # id for brands
    brand_id = 1
    # Iterate the list to acces every single word
    for input in input_list:
        # Convert word to lower-case
        input = access_str(input.lower())
        # Case 1: check if the word is a valid brand name
        if input in brands:
            output["brand"][0][brand_id] = input
            brand_id += 1
        # Case 2: if the word is misseplling but still in our unclear brand database
        elif input in unclear_brands.keys():
            output["brand"][0][brand_id] = unclear_brands[input]
            brand_id += 1
        # Case 3: correct the spelling and check if the word is in the brand list
        elif spell.correction(input) in brands:
            '''
            Here, we can write the incorrect brand name to the unclear brand database
            '''
            input = spell.correction(input)
            output["brand"][0][brand_id] = input
            brand_id += 1
        # Case 4: If not a brand, check if it is a state or country
        elif input in us_states.values():
            output['state'] = input
        elif input in country.keys():
            output['country'] = input
        # Case 5: check phone number
        elif input.isnumeric():
            output['ph no'] = input
    return output

def main():
    # Method 1: use terminal to run
    try:
        input = sys.argv[1:]
        s = " "
        input = s.join(input)
        print(extract_input(input))
    except:
        print("error")
    
    # Method 2: in-file run. uncomment this part and comment method 1
    '''
        input = ""
        print(extract_input(input))
    '''

if __name__ == '__main__':
    main()


