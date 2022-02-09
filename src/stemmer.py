import re

"""
Design choice:

Using regex for convenience if i need some prerequisite condition to change suffix.
Else, I use endswith, as it is much faster.

Example on time difference: 

    py -3.9 -mtimeit -s"import re" "re.match('^[a-z]+(at|bl|iz)$','fished')"
    500000 loops, best of 5: 504 nsec per loop

    λ py -3.9 -mtimeit -s"'fished'.endswith('at') or 'fished'.endswith('bl') or 'fished'.endswith('iz')"
    50000000 loops, best of 5: 5.78 nsec per loop

Does the same thing, but much faster to do with endswith.

Basically, all the things done with .endswith were things that are easily done that way. 
Others can likely be done, but it is a TODO for when project is completed for further optimization
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
        # [a-z]+: At least one character between vowel and s.
        # s: Makes sure it ends in s
        elif re.match('^[a-z]*[aeiou]+[a-z]+s$', token):
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
        if re.match('^[a-z]*[aeiou]+[^aeiou]+[a-z]*(eedly|eed)$', token):
            # Ends with eed, remove d
            if token.endswith('eed'):
                token = token[0:-1]
            # Ends with eedly, remove dly
            else:
                token = token[0:-3]

        else:
            # If word contains vowel and ends with ed, edly, ing, ingly, delete
            if re.match('^[a-z]*[aeiou]+[a-z]+(ed|edly|ing|ingly)$', token):
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
