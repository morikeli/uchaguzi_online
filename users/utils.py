import matplotlib.pyplot as plt
import base64
from io import BytesIO

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.get_value()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    
    return graph

def plot_graph(x, y):
    plt.switch_backend('AGG')
    plt.figure(figsize(10, 5))
    plt.title('Votes garnered')
    plt.plot(x, y)
    plt.xlabel('Aspirants')
    plt.ylabel('Total votes')
    plt.tight_layout()
    graph = get_graph()
    return graph
