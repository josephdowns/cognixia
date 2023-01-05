name = input("What is your name? ")
age = input("What is your age? ")
years_coding = input("How many years have you been coding? ")
first_lang = input("What was your first coding language? ")
second_lang = input("What was your second coding language? ")
third_lang = input("What was your third coding language? ")
first_fav_lang = input("What is your favorite programming language? ")
second_fav_lang = input("What is your next favorite programming language? ")
third_fav_lang = input("What is your next favorite programming language? ")
lang_set = (first_lang, second_lang, third_lang)
fav_set = [first_fav_lang, second_fav_lang, third_fav_lang]

user = {
  "name": name,
  "age": age,
  "years_coding": years_coding,
  "languages": lang_set,
  "favorites": fav_set,
  "intersection": set(lang_set).intersection(set(fav_set))
}

print(f"Name: {user['name']}")
print(f"Age: {user['age']}")
print(f"Years Coding: {user['years_coding']}")
print(f"Languages: {user['languages']}")