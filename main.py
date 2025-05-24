import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from code import simulation

def main():
    print("Hello from sumo!")


if __name__ == "__main__":
    simulation.simulation()

