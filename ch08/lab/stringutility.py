class StringUtility:
    def __init__(self, string):
        self.string = string

    def __str__(self):
        return self.string
    
    def vowels(self):
        # vowel_count = 0
        # for char in self.string:
        #     if char.lower() in "aeiou":
        #         vowel_count += 1

        # if vowel_count < 5:
        #     return str(vowel_count)
        # else:
        #     return "many"

        return str(len([char for char in self.string if char.lower() in 'aeiou'])) if len([char for char in self.string if char.lower() in 'aeiou']) < 5 else 'many'

        
    def bothEnds(self):
        # if len(self.string) <= 2:
        #     return ""
        # else:
        #     return self.string[:2] + self.string[-2:]

        return self.string[:2] + self.string[-2:] if len(self.string) > 2 else ''
        
    def fixStart(self):
        if len(self.string) <= 1:
            return self.string

        first_char = self.string[0]
        replaced_string = first_char + self.string[1:].replace(first_char, '*')
        return replaced_string
    
    def asciiSum(self):
        # total_sum = 0
        # for char in self.string:
        #     total_sum += ord(char)
        # return total_sum

        return sum(ord(char) for char in self.string)
    
    def cipher(self):
        shifted_string = ""
        for char in self.string:
            if char.isalpha():
                if char.islower():
                    ascii_offset = ord('a')
                    shifted_char = chr((ord(char) - ascii_offset + len(self.string)) % 26 + ascii_offset)
                else:
                    ascii_offset = ord('A')
                    shifted_char = chr((ord(char) - ascii_offset + len(self.string)) % 26 + ascii_offset)
            else:
                shifted_char = char
            shifted_string += shifted_char
        return shifted_string