import time
import statistics
import matplotlib.pyplot as plt
from blockchain import Blockchain
difficulty_values = [1, 2, 3, 4, 5]

transactions = [
    {'Sender': 'A', 'Beneficiary': 'B', 'Amount': 10},
    {'Sender': 'B', 'Beneficiary': 'C', 'Amount': 5},
    {'Sender': 'C', 'Beneficiary': 'D', 'Amount': 2},
    {'Sender': 'D', 'Beneficiary': 'E', 'Amount': 8},
    {'Sender': 'E', 'Beneficiary': 'F', 'Amount': 3},
]

def get_transaction(i):
    """Return transaction from list"""
    return transactions[i % len(transactions)]

average_times = []
mining_times_dict = {}

for difficulty in difficulty_values:

    print("\nTesting difficulty:", difficulty)

    blockchain = Blockchain(difficulty=difficulty)

    mining_times = []

    for i in range(5):

        transaction = get_transaction(i)

        start_time = time.time()

        blockchain.AjouterBlock(transaction)

        end_time = time.time()

        mining_time = end_time - start_time

        mining_times.append(mining_time)

        print(f"Block {i+1} mining time: {mining_time:.4f} seconds")
      
    avg_time = statistics.mean(mining_times)

    average_times.append(avg_time)

    mining_times_dict[difficulty] = mining_times

    print("Average mining time:", avg_time)

plt.plot(difficulty_values, average_times, marker='o')

plt.title("Mining Time vs Difficulty")
plt.xlabel("Difficulty")
plt.ylabel("Average Mining Time (seconds)")

plt.grid(True)

plt.savefig("mining_time_graph.png")

plt.show()
