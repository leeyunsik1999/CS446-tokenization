
# Timing Difference Examples
## Difference between regex and .endswith
Example on time difference: 

    py -3.9 -mtimeit -s"import re" "re.match('^[a-z]+(at|bl|iz)$','fished')"
    500000 loops, best of 5: 504 nsec per loop

    λ py -3.9 -mtimeit -s"'fished'.endswith('at') or 'fished'.endswith('bl') or 'fished'.endswith('iz')"
    50000000 loops, best of 5: 5.78 nsec per loop

Does the same thing, but much faster to do with endswith.

Basically, all the things done with .endswith were things that are easily done that way. 
Others can likely be done, but it is a TODO for when project is completed for further optimization

## Difference between .endswith and direct index comparisons of strings
Example on time difference between using .endswith and string index for last char:

    λ py -3.9 -mtimeit -s"import re" "s = 'example'" "if s.endswith('s'): s=s[0:-1]"
    5000000 loops, best of 5: 85 nsec per loop

    λ py -3.9 -mtimeit -s"import re" "s = 'example'" "if s[len(s)-1] == 's': s=s[0:-1]"
    5000000 loops, best of 5: 70.1 nsec per loop

Example 2

    λ py -3.9 -mtimeit -s"import re" "token = 'example'" "if token.endswith('ies') or token.endswith('ied'): token = token[0:-3] + ('i' if len(token) > 4 else 'ie')"                                        
    2000000 loops, best of 5: 144 nsec per loop

    λ py -3.9 -mtimeit -s"import re" "token = 'example'" "d = len(token)" "if token[d-3:d-2] == 'ie' and (token[d-1] == 'd' or token[d-1] == 's'): token = token[0:-3] + ('i' if len(token) > 4 else 'ie')"  
    5000000 loops, best of 5: 87.8 nsec per loop

Example 3

    λ py -3.9 -mtimeit -s"import re" "token = 'examplified'" "if token.endswith('ies') or token.endswith('ied'): token = token[0:-3] + ('i' if len(token) > 4 else 'ie')"
    1000000 loops, best of 5: 259 nsec per loop

    λ py -3.9 -mtimeit -s"import re" "token = 'examplified'" "d = len(token)" "if token[d-3:d-2] == 'ie' and (token[d-1] == 'd' or token[d-1] == 's'): token = token[0:-3] + ('i' if len(token) > 4 else 'ie')"
    5000000 loops, best of 5: 87.7 nsec per loop