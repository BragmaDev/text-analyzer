# CT30A3401 Distributed Systems
# Matti Bragge

from xmlrpc.server import SimpleXMLRPCServer
import math

PORT = 8001


# Finds the following counts of the given text:
# Character count, word count, average characters per word, median characters per word
# Text must be given as a list of lines
# Returns dictionary of results
def analyze_text(text):
    count_chars = 0
    words = []
    med_chars = 0

    # Create a single list of all words
    for line in text:
        count_chars += len(line)
        for word in line.split():
            words.append(word)

    # Conduct analysis     
    count_words = len(words)
    avg_chars = count_chars / count_words
    words_sorted = sorted(words, key=len)
    if count_words % 2 == 0:
        mid1 = len(words_sorted[int(count_words / 2) - 1])
        mid2 = len(words_sorted[int(count_words / 2)])
        med_chars = (mid1 + mid2) / 2
    else:
        med_chars = len(words_sorted[math.floor(count_words / 2)])

    # Create dict of results
    results = {
            "chars": count_chars, 
            "words": count_words, 
            "avg_chars": avg_chars, 
            "med_chars": med_chars
    }
    return results


def main():
    try:
        # Set up service
        server = SimpleXMLRPCServer(("127.0.0.1", PORT), allow_none=True)
        server.register_function(analyze_text, "analyze_text")
        server.serve_forever()
    except KeyboardInterrupt:
        return
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
    