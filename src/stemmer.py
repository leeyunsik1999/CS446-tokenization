import re

class Stemmer():
    def stem_a(token):
        """
        Stemmer logic for part 1a
        """
        # -sses --> ss
        if token.endswith('sses'):
            # -sses --> ss
            token = token[0:-len('sses')] + 'ss'
        # Pass if token ends with ss or us
        elif token.endswith('ss') or token.endswith('us'):
            pass
        # Ends with s + has a vowel not preceeding s: remove s
        # Initial [a-z]*: Anything before vowel.
        # [aeiou]+: At least one explicit vowel.
        # [a-z]+: At least one character between vowel and s.
        # s: Makes sure it ends in s
        elif re.match('^[a-z]*[aeiou]+[a-z]+s', token):
            token = token[0:-1]
        # Checks if token ends with ies or ied.
        # If so, checks token length. If >4 (preceeded by >=2 chars), replace last 3 chars with i. Else, replace with ie
        elif token.endswith('ies') or token.endswith('ied'):
            token = token[0:-3] + ('i' if len(token) > 4 else 'ie')

        # TODO: Remove if above is fine
        # # Check if suffix is ss or us. If it isn't, proceed with logic. Else, simply return the token
        # if not (token.endswith('ss') or token.endswith('us')):
        #     # -sses --> ss
        #     if token.endswith('sses'):
        #         token = token[0:-len('sses')] + 'ss'
        #     # Ends with s + has a vowel not preceeding s: remove s
        #     # Initial [a-z]*: Anything before vowel.
        #     # [aeiou]+: At least one explicit vowel.
        #     # [a-z]+: At least one character between vowel and s.
        #     # s: Makes sure it ends in s
        #     if re.match('^[a-z]*[aeiou]+[a-z]+s', token):
        #         token = token[0:-1]
        #     # Checks if token ends with ies or ied.
        #     # If so, checks token length. If >4 (preceeded by >=2 chars), replace last 3 chars with i. Else, replace with ie
        #     if token.endswith('ies') or token.endswith('ied'):
        #         token = token[0:-3] + ('i' if len(token) > 4 else 'ie')
        return token

    def stem_b(token):
        """
        Stemmer logic for part 1b
        """