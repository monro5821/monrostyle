text = input("Введите текст для анализа: ")

cleaned_text = ""
for char in text:
    if char in ".,!?:;\"'()[]-{}—":
        cleaned_text += " "
    else:
        cleaned_text += char

words = cleaned_text.lower().split()

if not words:
    print("Текст не содержит слов для анализа.")
else:
    total_words = len(words)
    unique_words = len(set(words))
    longest_word = max(words, key=len)

    most_common_word = max(set(words), key=words.count)
    most_common_count = words.count(most_common_word)

    temp_text = text.replace("!", ".").replace("?", ".")
    sentences = [s.strip() for s in temp_text.split(".") if s.strip()]
    sentence_count = len(sentences)

    avg_word_length = sum(len(word) for word in words) / total_words

    print("\n--- Результаты анализа текста ---")
    print(f"1. Общее количество слов: {total_words}")
    print(f"2. Количество уникальных слов: {unique_words}")
    print(f"3. Самое длинное слово: '{longest_word}' (длина: {len(longest_word)})")
    print(f"4. Самое частое слово: '{most_common_word}' (встречается {most_common_count} раз(а))")
    print(f"5. Количество предложений: {sentence_count}")
    print(f"6. Средняя длина слова: {avg_word_length:.2f} символов")
