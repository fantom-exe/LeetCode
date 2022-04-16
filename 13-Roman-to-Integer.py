class Solution:
    def roman_to_int(self, s: str) -> int:
        integer = 0
        for i in range(len(s)-1):
            prev_numeral = self.numeral_to_int(s[i-1])
            curr_numeral = self.numeral_to_int(s[i])

            if prev_numeral > curr_numeral or prev_numeral == curr_numeral:
                integer += self.numeral_to_int(curr_numeral)
            else:
                integer -= self.numeral_to_int(prev_numeral)

        print(integer)
        return integer

    @staticmethod
    def numeral_to_int(numeral):
        match numeral:
            case 'I':
                return 1
            case 'V':
                return 5
            case 'X':
                return 10
            case 'L':
                return 50
            case 'C':
                return 100
            case 'D':
                return 500
            case 'M':
                return 1000
            case _:
                return "Unknown numeral"


sol = Solution()
sol.roman_to_int('IV')
