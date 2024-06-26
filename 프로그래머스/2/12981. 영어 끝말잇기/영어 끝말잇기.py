def solution(n, words):
    used_words = set()
    previous_word = words[0]
    used_words.add(previous_word)
    
    for i in range(1, len(words)):
        current_word = words[i]
        
        if current_word in used_words or previous_word[-1] != current_word[0]:
            person = (i % n) + 1
            turn = (i // n) + 1
            return [person, turn]
        
        used_words.add(current_word)
        previous_word = current_word
    
    return [0, 0]
