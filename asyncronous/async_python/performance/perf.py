
import time


def count():
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("3")

def main():
    for i in range(3):
        count()


if __name__ == "__main__":
    t = time.perf_counter()
    main()
    t2 = time.perf_counter() - t
    print(f"Total time elapsed: {t2:0.2f}")