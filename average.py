import text_utils
import argparse
def line_count(filename):
    # Opens the file.
    file = open(filename, "r")
    # Lists all of the lines.
    lines = file.readlines()
    # Counts the amount of lines.
    line_count1 = len(lines)
    # Resets the count back to the beginning of the file.
    file.seek(0)
    # Reads all of the words in the file.
    words = (file.read())
    # Counts the amount of words in the file.
    wordcount = text_utils.count_words(words)
    # Closes the file.
    file.close()
    # Calculate the average amount of words in the file.
    return(wordcount/line_count1)
    
def main():
    parser = argparse.ArgumentParser(description='Count lines in a file.')
    parser.add_argument('filename', help='The fine to count lines from')
    args = parser.parse_args()

    count = line_count(args.filename)
    # Prints the average amount of words in the file.
    print(f"Average words per line: {count}")

if __name__ == '__main__':
    main()