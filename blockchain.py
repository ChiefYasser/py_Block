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


if __name__ == "__main__":

    difficulty = 4

    block1 = Block(
        index=1,
        transaction="Alice sends 10 BTC to Bob",
        previousHash="0000000000000",
        difficulty=difficulty
    )

    print(block1)
