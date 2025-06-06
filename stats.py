def count_words(phrase):
  count = len(phrase.split())
  return count

def count_letters(words):
  list_of_words_lowecase = (words.lower()).split()
  dic_of_letters = {}
  for word in list_of_words_lowecase:
    for letter in word:
      if letter not in dic_of_letters.keys():
        dic_of_letters[letter] = 1
      else:
        dic_of_letters[letter] += 1
    
  return dic_of_letters

def only_values(each_dict):
  return each_dict["num"]

def sorting(char_dictionary, counts):
  new_arranged_list = []
  for key, value in char_dictionary.items():
    if key.isalpha():
      new_arranged_dic = {}
      new_arranged_dic["char"] = key
      new_arranged_dic["num"] = value
      new_arranged_list.append(new_arranged_dic)
  
  new_arranged_list.sort(reverse=True, key=only_values)
  return new_arranged_list


