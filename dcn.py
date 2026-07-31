import tkinter as tk
import time
import threading
import matplotlib.pyplot as plt

# The original Tkinter GUI creation part causes an error in headless environments like Colab.
# root = tk.Tk()
# root.title("Network Topology Simulator")
# root.geometry("600x600")
# canvas = tk.Canvas(root, width=600, height=500, bg="white")
# canvas.pack()

# Draw Star Topology (adapted for Matplotlib)
def draw_star_matplotlib():
    plt.figure(figsize=(6, 5))
    plt.title("Star Topology")
    center = (3, 2) # Adjusted coordinates for better plotting
    nodes = [(1,1), (5,1), (1,3), (5,3)]

    # Draw center node
    plt.scatter(center[0], center[1], s=800, c='blue', label='Hub')
    plt.text(center[0], center[1], "Hub", ha='center', va='center', color='white')

    for i, node in enumerate(nodes):
        plt.scatter(node[0], node[1], s=600, c='green', label=f'Node {i+1}')
        plt.plot([center[0], node[0]], [center[1], node[1]], 'k-') # 'k-' for black line

    plt.xlim(0, 6)
    plt.ylim(0, 4)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.axis('off') # Hide axes
    plt.show()

# Draw Bus Topology (adapted for Matplotlib - placeholder, not fully converted)
def draw_bus_matplotlib():
    plt.figure(figsize=(6, 5))
    plt.title("Bus Topology")
    nodes = [(1,2), (2,2), (3,2), (4,2), (5,2)]

    plt.plot([0.5, 5.5], [2, 2], 'k-', linewidth=3) # Bus line

    for i, node in enumerate(nodes):
        plt.scatter(node[0], node[1], s=600, c='green', label=f'Node {i+1}')

    plt.xlim(0, 6)
    plt.ylim(1, 3)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.axis('off')
    plt.show()

# Draw Ring Topology (adapted for Matplotlib - placeholder, not fully converted)
def draw_ring_matplotlib():
    plt.figure(figsize=(6, 5))
    plt.title("Ring Topology")
    nodes = [(3,1), (4.5,2), (4,3.5), (2,3.5), (1.5,2)]

    for i in range(len(nodes)):
        x1, y1 = nodes[i]
        x2, y2 = nodes[(i+1)%len(nodes)]
        plt.plot([x1, x2], [y1, y2], 'k-')

    for i, node in enumerate(nodes):
        plt.scatter(node[0], node[1], s=600, c='green', label=f'Node {i+1}')

    plt.xlim(0, 6)
    plt.ylim(0, 4.5)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.axis('off')
    plt.show()

# Since interactive GUI is not possible, we can directly call a drawing function
# to display a static image of one of the topologies.
draw_star_matplotlib()
draw_bus_matplotlib()
draw_ring_matplotlib()

# The original simulation logic and button creation are removed as they rely on Tkinter GUI.
# def simulate():
#     for i in range(5):
#         canvas.create_text(300, 450, text="Sending Data...", fill="red", font=("Arial", 14))
#         root.update()
#         time.sleep(0.5)
#         canvas.delete("all")
#         time.sleep(0.5)

# def run_simulation():
#     threading.Thread(target=simulate).start()

# btn_star = tk.Button(root, text="Star Topology", command=draw_star)
# btn_star.pack(pady=5)

# btn_bus = tk.Button(root, text="Bus Topology", command=draw_bus)
# btn_bus.pack(pady=5)

# btn_ring = tk.Button(root, text="Ring Topology", command=draw_ring)
# btn_ring.pack(pady=5)

# btn_sim = tk.Button(root, text="Simulate Data Flow", command=run_simulation)
# btn_sim.pack(pady=10)

# root.mainloop()