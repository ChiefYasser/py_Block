import hashlib
from datetime import datetime
class Block:

    def __init__(self, index, transaction, previousHash, difficulty):
        """Constructor for Block object"""
        self.index = index
        self.transaction = transaction
        self.previousHash = previousHash
        self.difficulty = difficulty
        self.timestamp = datetime.now()
        self.nonce = 0
        self.hash = self.mineBlock()
    def __str__(self):
        return f"""
Block Index: {self.index}
Timestamp: {self.timestamp}
Difficulty: {self.difficulty}
Nonce: {self.nonce}
Transactions: {self.transaction}
Previous Hash: {self.previousHash}
Hash: {self.hash}
"""

    def calculHash(self):
        """Calculate SHA256 hash of the block"""
        data = (
            str(self.index) +
            str(self.timestamp) +
            str(self.nonce) +
            str(self.transaction) +
            str(self.previousHash)
        )

        encodedData = data.encode('ascii')
        hashValue = hashlib.sha256(encodedData).hexdigest()

        return hashValue

    def mineBlock(self):
        """Mining process to find a valid hash"""
        prefix = "0" * self.difficulty

        while True:
            hashValue = self.calculHash()

            if hashValue.startswith(prefix):
                return hashValue
            else:
                self.nonce += 1

class Blockchain:

    def __init__(self, difficulty=3):
        """Constructor for Blockchain"""
        self.chain = []
        self.index = 0
        self.difficulty = difficulty

        # Genesis Block
        genesis_block = Block(
            index=0,
            transaction="Genesis Block",
            previousHash="0" * 64,
            difficulty=self.difficulty
        )

        self.chain.append(genesis_block)

    def getLastBlock(self):
        """Return the last block of the chain"""
        return self.chain[-1]

    def AjouterBlock(self, transaction):
        """Add a new block to the blockchain"""

        self.index += 1

        new_block = Block(
            index=self.index,
            transaction=transaction,
            previousHash=self.getLastBlock().hash,
            difficulty=self.difficulty
        )

        self.chain.append(new_block)

    def checkChainValid(self):
        """Verify if the blockchain is valid"""

        for i in range(1, len(self.chain)):

            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check if the stored hash is correct
            if current_block.hash != current_block.calculHash():
                return False

            # Check if previous hash matches
            if current_block.previousHash != previous_block.hash:
                return False

        return True
if __name__ == "__main__":

    blockchain = Blockchain(difficulty=3)

    blockchain.AjouterBlock("Alice sends 10 BTC to Bob")
    blockchain.AjouterBlock("Bob sends 5 BTC to Charlie")
    blockchain.AjouterBlock("Charlie sends 2 BTC to David")

    print("\n----- BLOCKCHAIN -----")

    for block in blockchain.chain:
        print(block)

    print("Blockchain valid:", blockchain.checkChainValid())
