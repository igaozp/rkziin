class CompressedGene:
    def __init__(self, gene: str) -> None:
        self._compress(gene)

    def _compress(self, gene: str) -> None:
        # start with sentinel
        self.bit_string: int = 1

        for nucleotide in gene.upper():
            # shift left two bits
            self.bit_string <<= 2
            if nucleotide == "A":
                # change last two bits to 00
                self.bit_string |= 0b00
            elif nucleotide == "C":
                # change last two bits to 01
                self.bit_string |= 0b01
            elif nucleotide == "G":
                # change last two bits to 10
                self.bit_string |= 0b10
            elif nucleotide == "T":
                # change last two bits to 11
                self.bit_string |= 0b11
            else:
                raise ValueError("Invalid Nucleotide:{}".format(nucleotide))

    def decompress(self) -> str:
        gene: str = ""
        for i in range(0, self.bit_string.bit_length() - 1, 2):
            bits: int = self.bit_string >> i & 0b11
            if bits == 0b00:
                gene += "A"
            elif bits == 0b01:
                gene += "C"
            elif bits == 0b10:
                gene += "G"
            elif bits == 0b11:
                gene += "T"
            else:
                raise ValueError("Invalid bits:{}".format(bits))
        return gene[::-1]

    def __str__(self) -> str:
        return self.decompress()


if __name__ == '__main__':
    from sys import getsizeof

    original: str = "TAGGGATTAACCGTTATATATATATAGCCATGGATCGATT" \
                    "ATATAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATA" * 100
    print("original is {} bytes".format(getsizeof(original)))
    compressed: CompressedGene = CompressedGene(original)
    print("compressed is {} bytes".format(getsizeof(compressed.bit_string)))
    print(compressed)
    print("original and decompressed are the same: {}".format(original ==
                                                              compressed.decompress()))
