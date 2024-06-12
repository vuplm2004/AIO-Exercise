def exercise1(tp, fp, fn):
    if not isinstance(tp, int):
        print("tp must be int")
    elif not isinstance(fp, int):
        print("fp must be int")
    elif not isinstance(fn, int):
        print("fn must be int")
    else:
        if tp > 0 and fp > 0 and fn > 0:
            precision = tp / (tp + fp)
            recall = tp / (tp + fn)
            f1_score = 2 * (precision * recall) / (precision + recall)

            print(f"precision is {precision}")
            print(f"recall is {recall}")
            print(f"f1_score is {f1_score}")
        else:
            print("tp and fp and fn must be greater than zero")


if __name__ == "__main__":
    exercise1(tp=2, fp=3, fn=4)
    exercise1(tp="a", fp=3, fn=4)
    exercise1(tp=2, fp="a", fn=4)
    exercise1(tp=2, fp=3, fn="a")
    exercise1(tp=2, fp=3, fn=0)
    exercise1(tp=2.1, fp=3, fn=4)
