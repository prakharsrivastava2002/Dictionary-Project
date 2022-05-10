import json 
from difflib import get_close_matches 
data = json.load(open("data.json"))

def translate (word) :
      word = word.lower()
      if word in data :
        return data[word]
      elif word.title() in data :
        return data[word.title()]
      elif word.upper() in data :
        return data[word.upper()]
      elif len(get_close_matches(word,data.keys())) > 0 :
        yn = input("Did you mean %s Instead?. Please Enter Y if yes and N if No : \n " % get_close_matches(word,data.keys())[0])
        if yn == "Y" or yn == "y" :
          return list(data[get_close_matches(word,data.keys())[0]])
        elif yn== "N" or yn == "n":
          return "Sorry the Word doesn't Exist "
        else :
          return "Sorry we didn't understand your Entry"  
      else :
        return "The word does not exist. Please re-check it."    

word = input ("Enter the word to be searched :  ")
print (translate(word))

