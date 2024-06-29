import time

def createbox():
    border = '-+-' * 10
    print(border)
    print()
    print('Enter the phrase as fast as possible and with accuracy')
    print()

def typing_speed_test():
    string = "Python is an interpreted, high-level programming language"
    word_count = len(string.split())

    while True:
        t0 = time.time()
        createbox()
        print(string, '\n')
        input_text = input()
        t1 = time.time()

        length_of_input = len(input_text.split())
        accuracy = len(set(input_text.split()) & set(string.split())) / word_count
        time_taken = t1 - t0
        words_per_minute = (length_of_input / time_taken) * 60

        # Showing results now
        print('Total words \t :', length_of_input)
        print('Time used \t :', round(time_taken, 2), 'seconds')
        print('Your accuracy \t :', round(accuracy * 100, 2), '%')
        print('Speed is \t :', round(words_per_minute, 2), 'words per minute')

        retry = input("Do you want to retry? (yes/no): ").strip().lower()
        if retry != 'yes':
            print('Thank you, bye bye.')
            time.sleep(1.5)
            break

if __name__ == "__main__":
    typing_speed_test()
