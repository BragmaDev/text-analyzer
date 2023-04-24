# CT30A3401 Distributed Systems
# Matti Bragge

from xmlrpc.server import SimpleXMLRPCServer
from bokeh.layouts import row
from bokeh.plotting import figure, output_file, save

P1_LABELS = ['Characters', 'Words']
P2_LABELS = ['Average characters per word', 'Median of characters per word']
PORT = 8002


# Takes in a dictionary that includes the counts defined in P1_LABELS and P2_LABELS
# Returns a dictionary with:
# - boolean indicating visualization success
# - visualization filename
def visualize_results(results):
    p1_results = [results["chars"], results["words"]]
    p2_results = [results["avg_chars"], results["med_chars"]]

    filename = "visualization.html"
    output_file(filename, title="Analysis results")

    p1 = figure(x_range=P1_LABELS, height=350, title="Analysis results",
            toolbar_location=None, tools="")
    p1.vbar(x=P1_LABELS, top=p1_results, width=0.9)
    p1.xgrid.grid_line_color = None
    p1.y_range.start = 0

    p2 = figure(x_range=P2_LABELS, height=350, title="",
            toolbar_location=None, tools="")
    p2.vbar(x=P2_LABELS, top=p2_results, width=0.9)
    p2.xgrid.grid_line_color = None
    p2.y_range.start = 0

    try:
        save(row(p1, p2))
        return {"success": True, "filename": filename}
    except:
        return {"success": False, "filename": filename}


def main():
    try:
        # Set up service
        server = SimpleXMLRPCServer(("127.0.0.1", PORT), allow_none=True)
        server.register_function(visualize_results, "visualize_results")
        server.serve_forever()
    except KeyboardInterrupt:
        return
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
    