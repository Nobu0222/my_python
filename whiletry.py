import sys

while(1):

    try:
        print("数字を入力してください")
        a=int(input())
        break
    except ValueError:
        print("すうじをにゅうりょくしてください")
        continue

print("よくできました！%dポイント！"%a)