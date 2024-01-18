import random
when=['A few years ago', 'Yesterday', 'Last night', 'A long time ago', 'On 20th January']
who=['a rabbit', 'an elephant', 'a mouse', 'a turtle', 'a cat']
name=['Ali', 'Miriam', 'Daniel', 'Hoouk', 'Starwalker']
residence=['Barcelona', 'India', 'Germany', 'Venice', 'England']
went=['the cinema', 'university', 'the seminar', 'school', 'the laundry']
happened=['made a lot of friends','eats a burger', 'found a secret key', 'solved a mistery', 'wrote a book']

print(random.choice(when)+', '+random.choice(who)+' that lived in '+random.choice(residence)+', went to '+random.choice(went)+' and '+random.choice(happened)+'.')