from typing import List


class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        output = ""
        for i in strs:
            output += i + "ahksdjb$hajd62"
        return output

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        return s.split("ahksdjb$hajd62")[:-1]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))