from itertools import permutations

def solve_cryptarithmetic(words, result):
    unique_chars = set(''.join(words) + result)
    
    if len(unique_chars) > 10:
        return None
    
    for perm in permutations(range(10), len(unique_chars)):
        char_to_digit = {char: digit for char, digit in zip(unique_chars, perm)}
        
        if all(char_to_digit[word[0]] != 0 for word in words + [result]):
            eval_words = [int(''.join(str(char_to_digit[char]) for char in word)) for word in words]
            eval_result = int(''.join(str(char_to_digit[char]) for char in result))
            
            if sum(eval_words) == eval_result:
                return {char: digit for char, digit in zip(unique_chars, perm)}
    
    return None

words = ["SEND", "MORE"]
result = "MONEY"
solution = solve_cryptarithmetic(words, result)
print("Dhruv Varshney \nA2305221157")
print(solution)