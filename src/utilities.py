import time

class Utilities:
    @staticmethod
    def clear(lines=32):
        print("\n"*lines)

    @staticmethod
    def closeServer():
        Utilities.clear()
        print("!=====Goodbye=====!")
        time.sleep(0.75)
        Utilities.clear()
        exit()

    @staticmethod
    def next():
        input('Pres [ENTER] to continue')
