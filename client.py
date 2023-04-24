# CT30A3401 Distributed Systems
# Matti Bragge

import xmlrpc.client

INPUT_PORT = 8000
ANALYZER_PORT = 8001
VISUALIZER_PORT = 8002

input_proxy = xmlrpc.client.ServerProxy(f"http://127.0.0.1:{INPUT_PORT}/")
analyzer_proxy = xmlrpc.client.ServerProxy(f"http://127.0.0.1:{ANALYZER_PORT}/")
visualizer_proxy = xmlrpc.client.ServerProxy(f"http://127.0.0.1:{VISUALIZER_PORT}/")


# Returns a dictionary with:
# - boolean that indicates if the input is valid
# - the input text as a list of lines
def request_input_service(input_filename):
    try:
        response = input_proxy.validate_input(input_filename)
        return response
    except Exception as e:
        print(e)
        return {"success": False}


# Returns analysis results as a dictionary
def request_analyzer_service(text_lines):
    try:
        response = analyzer_proxy.analyze_text(text_lines)
        return response
    except Exception as e:
        print(e)
        return None


# Returns a dictionary with:
# - boolean indicating visualization success
# - visualization filename
def request_visualizer_service(results):
    try:
        response = visualizer_proxy.visualize_results(results)
        return response
    except Exception as e:
        print(e)
        return {"success": False}


# Prints the results given by the analyzer service
def print_analysis_results(results):
    print("\n----------------------------")
    print("Characters: ", results["chars"])
    print("Words: ", results["words"])
    print("Average characters per word: ", results["avg_chars"])
    print("Median of characters per word: ", results["med_chars"])
    print("----------------------------")


def main():   
    print("\nTextAnalyzer - RPC Application")
    print("==========================")
    filename = input("Enter input filename:\n")
    filename = filename.strip()
    
    # Input service RPC
    response = request_input_service(filename)
    if response["valid"] == False:
        print("Invalid input, check that the file exists and that it does not consist of only whitespaces.")
        return

    # Analyzer service RPC
    response = request_analyzer_service(response["input_text"])
    if response == None:
        print("Analysis failed due to an error.")
        return     
    print_analysis_results(response)

    # Visualizer service RPC
    response = request_visualizer_service(response)
    if response["success"] == False:
        print("Visualization could not be created due to an error.")
        return
    else:
        print(f"Visualization created as '{response['filename']}'.")


if __name__ == '__main__':
    main()