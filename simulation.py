import random
print("GitHub history test")

print("=== Edge vs Cloud Simulation ===")

def simulate():
    
    edge_latency = random.uniform(10, 30)
    cloud_latency = random.uniform(50, 100)

    print(f"Edge latency : {edge_latency:.2f} ms")
    print(f"Cloud latency: {cloud_latency:.2f} ms")

    if edge_latency < cloud_latency:
        print("Edge is faster.")
    else:
        print("Cloud is faster.")


if __name__ == "__main__":
    simulate()