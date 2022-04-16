class Solution:
    def roman_to_int(self, s: str) -> int:
        i_store = 0  # count I numerals
        integer = 0
        for numeral in s:
            if
                integer += self.numeral_to_int(numeral)

        if i_store > 0:
            integer += i_store

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
sol.roman_to_int('VX')
