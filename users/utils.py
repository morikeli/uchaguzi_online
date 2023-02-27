import matplotlib.pyplot as plt
import base64
from io import BytesIO

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    
    return graph

def plot_graph(x, y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(5, 7))
    plt.title('Votes garnered')
    plt.bar(x, y)
    plt.xlabel('Aspirants')
    plt.ylabel('Total votes')
    plt.xticks(rotation=60)
    plt.tight_layout()
    graph = get_graph()
    return graph
