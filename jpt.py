import random

hiragana_dict = {
    "あ": "a",   "い": "i",   "う": "u",   "え": "e",   "お": "o",
    "か": "ka",  "き": "ki",  "く": "ku",  "け": "ke",  "こ": "ko",
    "さ": "sa",  "し": "shi", "す": "su",  "せ": "se",  "そ": "so",
    "た": "ta",  "ち": "chi", "つ": "tsu", "て": "te",  "と": "to",
    "な": "na",  "に": "ni",  "ぬ": "nu",  "ね": "ne",  "の": "no",
    "は": "ha",  "ひ": "hi",  "ふ": "fu",  "へ": "he",  "ほ": "ho",
    "ま": "ma",  "み": "mi",  "む": "mu",  "め": "me",  "も": "mo",
    "や": "ya",              "ゆ": "yu",              "よ": "yo",
    "ら": "ra",  "り": "ri",  "る": "ru",  "れ": "re",  "ろ": "ro",
    "わ": "wa",                          "を": "wo",
    "ん": "n",
    # Dakuten (voiced consonants)
    "が": "ga",  "ぎ": "gi",  "ぐ": "gu",  "げ": "ge",  "ご": "go",
    "ざ": "za",  "じ": "ji",  "ず": "zu",  "ぜ": "ze",  "ぞ": "zo",
    "だ": "da",  "ぢ": "ji",  "づ": "zu",  "で": "de",  "ど": "do",
    "ば": "ba",  "び": "bi",  "ぶ": "bu",  "べ": "be",  "ぼ": "bo",
    # Handakuten (p-sounds)
    "ぱ": "pa",  "ぴ": "pi",  "ぷ": "pu",  "ぺ": "pe",  "ぽ": "po",
    # Small characters
    "ぁ": "a",   "ぃ": "i",   "ぅ": "u",   "ぇ": "e",   "ぉ": "o",
    "ゃ": "ya",  "ゅ": "yu",  "ょ": "yo",  "っ": "tsu", "ゎ": "wa",
}

katakana_dict = {
    "ア": "a",   "イ": "i",   "ウ": "u",   "エ": "e",   "オ": "o",
    "カ": "ka",  "キ": "ki",  "ク": "ku",  "ケ": "ke",  "コ": "ko",
    "サ": "sa",  "シ": "shi", "ス": "su",  "セ": "se",  "ソ": "so",
    "タ": "ta",  "チ": "chi", "ツ": "tsu", "テ": "te",  "ト": "to",
    "ナ": "na",  "ニ": "ni",  "ヌ": "nu",  "ネ": "ne",  "ノ": "no",
    "ハ": "ha",  "ヒ": "hi",  "フ": "fu",  "ヘ": "he",  "ホ": "ho",
    "マ": "ma",  "ミ": "mi",  "ム": "mu",  "メ": "me",  "モ": "mo",
    "ヤ": "ya",              "ユ": "yu",              "ヨ": "yo",
    "ラ": "ra",  "リ": "ri",  "ル": "ru",  "レ": "re",  "ロ": "ro",
    "ワ": "wa",                          "ヲ": "wo",
    "ン": "n",
    # Dakuten (voiced consonants)
    "ガ": "ga",  "ギ": "gi",  "グ": "gu",  "ゲ": "ge",  "ゴ": "go",
    "ザ": "za",  "ジ": "ji",  "ズ": "zu",  "ゼ": "ze",  "ゾ": "zo",
    "ダ": "da",  "ヂ": "ji",  "ヅ": "zu",  "デ": "de",  "ド": "do",
    "バ": "ba",  "ビ": "bi",  "ブ": "bu",  "ベ": "be",  "ボ": "bo",
    # Handakuten (p-sounds)
    "パ": "pa",  "ピ": "pi",  "プ": "pu",  "ペ": "pe",  "ポ": "po",
    # Small characters
    "ァ": "a",   "ィ": "i",   "ゥ": "u",   "ェ": "e",   "ォ": "o",
    "ャ": "ya",  "ュ": "yu",  "ョ": "yo",  "ッ": "tsu", "ヮ": "wa" 
}


def test():
    while True:

        win = 0
        loss = 0

        print("Welcome to the Japanese Language test!")
        try:
            mode = int(input("-----\n1: Hiragana\n2: Katakana\n3: Mix\n0: Quit "))

            if mode == 1:
                for i in range(15):
                    ai = random.choice(list(hiragana_dict))
                    entry = input(f"{ai} : ").lower().strip()

                    if hiragana_dict[ai] == entry:
                        print("That's correct")
                        win += 1
                    else:
                        print(f"That's incorrect. Correct answer was: {hiragana_dict[ai]}")
                        loss += 1

            elif mode == 2:
                for i in range(15):
                    ai = random.choice(list(katakana_dict))
                    entry = input(f"{ai} : ").lower().strip()

                    if katakana_dict[ai] == entry:
                        print("That's correct")
                        win += 1
                    else:
                        print(f"That's incorrect. Correct answer was: {katakana_dict[ai]}")
                        loss += 1

            elif mode == 3:
                mix_dict = {**hiragana_dict, **katakana_dict}

                for i in range(15):
                    ai = random.choice(list(mix_dict))
                    entry = input(f"{ai} : ").lower().strip()
                    
                    if mix_dict[ai] == entry:
                        print("That's correct")
                    else:
                        print(f"That's incorrect. Correct answer was: {mix_dict[ai]}")
            
            elif mode == 0:
                print("Goodbye..")
                break

            else:
                raise ValueError
                
            
            print(f"{win} correct answers and {loss} loses in 15 characters")
        
        except ValueError:
            print("Please enter a valid number")

if __name__ == "__main__":
    test()