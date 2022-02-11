import re

"""
Design choice:

Using regex for convenience if i need some prerequisite condition to change suffix.
Else, I use endswith, as it is much faster, or direct string indexing. 

Specific tests run to calculate time improvements is in README.

Essentially, I tried to avoid using regex for initial processing (if/else checks) as much as possible.
"""
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
        # [a-z]*: Any number of characters between s and initial vowel
        # s: Makes sure it ends in s
        # NOTE: This step done after ss/us detection so we don't need regex to detect and skip -ss/us words
        # Checking if string ends with s first as it makes it much faster to detect words not ending that way
        # Using string index is faster than .endswith
        elif token[len(token)-1] == 's':
            if re.match('^[a-z]*[aeiou][a-z]+s$', token):
                token = token[0:-1]

        # Checks if token ends with ies or ied.
        # If so, checks token length. If >4 (preceeded by >=2 chars), replace last 3 chars with i. Else, replace with ie
        elif token.endswith('ies') or token.endswith('ied'):
            token = token[0:-3] + ('i' if len(token) > 4 else 'ie')

        return token

    def stem_b(token):
        """
        Stemmer logic for part 1b
        """
        # Replacing eed/eedly with ee if 
        # Start with checking eed/eedly as regex takes much longer to run
        if token.endswith('eed') or token.endswith('eedly'):
            if re.match('^[a-z]*[aeiou]+[^aeiou]+[a-z]*(eedly|eed)$', token):
                # Ends with eed, remove d
                if token.endswith('eed'):
                    token = token[0:-1]
                # Ends with eedly, remove dly
                else:
                    token = token[0:-3]

        else:
            # If word contains vowel and ends with ed, edly, ing, ingly, delete
            # Checking it ends first as it's much faster this way
            if token.endswith('ed') or token.endswith('edly') or token.endswith('ing') or token.endswith('ingly'):
                if re.match('^[a-z]*[aeiou]+[a-z]+$', token):
                    if token.endswith('ed'):
                        token = token[0:-2]
                    elif token.endswith('edly'):
                        token = token[0:-4]
                    elif token.endswith('ing'):
                        token = token[0:-3]
                    else:
                        token = token[0:-5]

                    # Adding e if token ends with at, bl or iz.
                    if token.endswith('at') or token.endswith('bl') or token.endswith('iz'):
                        token += 'e'

                    # Double letter not ending in ll, ss or zz
                    elif (len(token) > 2) and (token[len(token)-1] == token[len(token)-2]) and not (token[len(token)-1] == 'l' or token[len(token)-1] == 's' or token[len(token)-1] == 'z'):
                        token = token[0:-1]

                    elif len(token) < 4:
                        token += 'e'
                    
        return token
