import re
import sys
import os

current_dir = os.path.dirname(os.path.realpath(__file__))
filepath = current_dir+"/books.csv"                     #Please make sure that the file books.csv is in the same dir.

#bookID,title,authors,average_rating,isbn,isbn13,language_code,  num_pages,ratings_count,text_reviews_count,publication_date,publisher
#1,Harry Potter and the Half-Blood Prince (Harry Potter  #6),J.K. Rowling/Mary GrandPré,4.57,0439785960,9780439785969,eng,652,2095690,27591,9/16/2006,Scholastic Inc.
#2034,Comoediae 1: Acharenses/Equites/Nubes/Vespae/Pax/Aves,Aristophanes/F.W. Hall/W.M. Geldart,5.00,0198145047,9780198145042,grc,364,0,0,2/22/1922,Oxford University Press  USA

def run():

    pattern = re.compile(r'^([0-9]*\s?),(\s?.*\s?),(\s?.*\s?),(\s?5\.00\s?),(.*)$')

    f = open(filepath, 'r', encoding='utf-8')

    most_rated_books = []

    Total = 0

    for line in f:
        res = re.match(pattern, line)
        
        if res:
            print('')
            print(f'BookID: {res.group(1)}, Title: {res.group(2)}, Authors: {res.group(3)}, Rating: {res.group(4)}')
            print(f'Aditional Info: {res.group(5)}')
            print('')
            Total +=1
            most_rated_books.append(res)
    print(f'We find {Total} books rating as 5.0 !')

    f.close()

if __name__ == '__main__':

    print('The following list shows the most rated books in the library:')
    run()