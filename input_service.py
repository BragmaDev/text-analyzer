# CT30A3401 Distributed Systems
# Matti Bragge

from xmlrpc.server import SimpleXMLRPCServer

PORT = 8000


# Reads a text file and returns it as a list of lines with newline characters removed
def read_file(filename):
    # Read input file
    input_text = []
    try:
        file = open(filename, "r", encoding="utf-8")
        for line in file:
            # Remove newline characters
            input_text.append(line.rstrip("\n"))
        return input_text
    except Exception as e:
        print(e)
        return ""


# Checks that the input does not consist of only whitespaces
# Returns a dictionary with:
# - boolean that indicates if the input is valid
# - the input text as a list of lines
def validate_input(filename):
    input_text = read_file(filename)
    full_string = ""
    for line in input_text:
        full_string += line
    if full_string.strip() == "":
        return {"valid": False, "input_text": input_text}
    return {"valid": True, "input_text": input_text}


def main():   
    try:
        # Set up service
        server = SimpleXMLRPCServer(("127.0.0.1", PORT), allow_none=True)
        server.register_function(validate_input, "validate_input")
        server.serve_forever()
    except KeyboardInterrupt:
        return
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()