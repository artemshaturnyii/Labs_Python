import csv
import random
import xml.etree.ElementTree as ET


### Task 1
### Code for the first task full like we did in class
def find_titles_longer_30(books):
    books.seek(0)
    reader = csv.DictReader(books, delimiter=';')
    books_names = []
    number_of_books = 0

    for row in reader:
        book_title = row['Book-Title']
        books_names.append(book_title)

    for title in books_names:
        if len(title) > 30:
            number_of_books += 1
            ### print(title, end='   ')           ### Printing the title
            ### print(len(title))                 ### Printing the number of symbols, was used for checking

    print(f"The number of records where the Title field string is longer than 30 characters is: {number_of_books}")


### Shorter code with no additional massive and with using one cycle
def find_titles_longer_30_short(books):
    books.seek(0)
    reader = csv.DictReader(books, delimiter=';')
    number_of_books = 0

    for row in reader:
        book_title = row['Book-Title']
        if len(book_title) > 30:
            number_of_books += 1
            ### print(book_title, end='   ')      ### Printing the title
            ### print(len(book_title))            ### Printing the number of symbols, was used for checking

    print(f"The number of records where the Title field string is longer than 30 characters is: {number_of_books}")
    print()


### Task 2
def find_the_book_by_author(books):
    books.seek(0)
    reader = csv.DictReader(books, delimiter=';')
    book_year = 0

    print("Write the Author to find the books (after 2000 year only!): ", end='')
    author_name = input()

    for row in reader:
        book_year = int(row['Year-Of-Publication'])
        if (book_year > 2000) and (author_name == row['Book-Author']):
            print(row['Year-Of-Publication'], '|', row['Book-Title'])


### Task 3
def check_presence_in_list(list_references, row_for_import):
    return row_for_import in list_references


def generate_bibliographic_references(books):
    books.seek(0)
    reader = csv.reader(books, delimiter=';')

    max_number_of_books = 20
    filled_positions = 0
    list_references = []

    all_rows = list(reader)[1:]
    number_of_lines = len(all_rows)

    while filled_positions < max_number_of_books and filled_positions < number_of_lines:
        row_number_for_import = random.randint(0, number_of_lines - 1)
        row_for_import = all_rows[row_number_for_import]

        if not check_presence_in_list(list_references, row_for_import):
            list_references.append(row_for_import)
            filled_positions += 1

    return list_references


def create_txt_file(list_references, filename="references.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        for index, row in enumerate(list_references, start=1):
            author = row[2].strip()
            title = row[1].strip()
            year = row[3].strip()
            f.write(f"{index}. {author}. {title} - {year}\n")


### Task 4
def parse_and_extract_xml_file(file_name="currency.xml"):
    xml_tree = ET.parse(file_name)
    xml_root = xml_tree.getroot()

    currency_dictionary = {}

    for valute_node in xml_root.findall("Valute"):
        currency_name = valute_node.find("Name").text.strip()
        currency_char_code = valute_node.find("CharCode").text.strip()
        currency_dictionary[currency_name] = currency_char_code

    for currency_name, currency_char_code in currency_dictionary.items():
        print(f"{currency_name} - {currency_char_code}")

    return currency_dictionary


### Task 5
def output_list_of_unique_publishers(books):
    books.seek(0)
    csv_reader = csv.DictReader(books, delimiter=';')

    list_of_all_publishers = []
    for row in csv_reader:
        list_of_all_publishers.append(row['Publisher'])

    unique_publishers = set(list_of_all_publishers)

    print("List of unique publishers:")
    for publisher in unique_publishers:
        print(publisher)

    return unique_publishers


### Task 6
def output_top_20_most_popular_books(books):
    books.seek(0)
    csv_reader = csv.DictReader(books, delimiter=';')

    list_of_books_with_downloads = []
    for row in csv_reader:
        book_title = row['Book-Title']
        downloads = int(row['Downloads'])
        list_of_books_with_downloads.append((book_title, downloads))

    list_of_books_with_downloads.sort(key=lambda x: x[1], reverse=True)

    print("Top 20 most popular books (by downloads):")
    top_count = min(20, len(list_of_books_with_downloads))
    for rank in range(top_count):
        book_title, total_downloads = list_of_books_with_downloads[rank]
        print(f"{rank+1}. {book_title} - {total_downloads} downloads")


### Main body of program
with open('books-en.csv') as books:
    ### Task 1
    find_titles_longer_30(books)
    find_titles_longer_30_short(books)

    ### Task 2
    find_the_book_by_author(books)

    ### Task 3
    create_txt_file(generate_bibliographic_references(books))

    ### Task 5
    output_list_of_unique_publishers(books)

    ### Task 6
    output_top_20_most_popular_books(books)

    ### Task 4
    parse_and_extract_xml_file("currency.xml")
