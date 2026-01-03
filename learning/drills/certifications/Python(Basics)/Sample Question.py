
def transformSentence(sentence):
    words = sentence.split()
    transformed_words = []
    for word in words:
        if not word:
            transformed_words.append("")
            continue
        new_chars = [word[0]]
        for i in range(1, len(word)):
            prev_char = word[i-1]
            curr_char = word[i]
            if prev_char < curr_char:
                new_chars.append(curr_char.upper())
            elif prev_char > curr_char:
                new_chars.append(curr_char.lower())
            else:
                new_chars.append(curr_char)
        transformed_words.append(''.join(new_chars))
    return ' '.join(transformed_words)


if __name__ == '__main__':
    sentence = input().strip()
    result = transformSentence(sentence)
    print(result)


