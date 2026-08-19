min = 42
sec = 42
total_sec = min * 60 + sec
print("Total seconds =", total_sec)
km = 10
mile = km * 1.61
print("Miles =", mile)
pace_sm = total_sec / mile
print("Pace in sec/mile =", pace_sm)
total_min = min + sec / 60
pace_mm = total_min / mile
print("Pace in min/mile =", pace_mm)
hour = total_min / 60
av_speed = mile / hour
print("Average speed in mile/hour =", av_speed)
import math
r = 5
v = 4/3 * math.pi * r ** 3
print("volume =", v)
x = 42
print("1 ~", (math.sin(x)) ** 2 + (math.cos(x)) ** 2)
print(math.e ** 2)
print(math.pow(2, 2))
print(math.exp(2))
def print_right(text):
    column_width = 40
    text_length = len(text)
    print(" " * (column_width - text_length), text)
print_right("Hi!")
print_right("Hey!")
print_right("Hello!")
print_right("Whassup!")
def triangle(text, height):
    for i in range(height):
        print(text * i)
triangle("L", 10)
def rectangle(text, width, height):
    for i in range(height):
        print(text * width)
rectangle("L", 20, 5)
def line_1(n, lyrics):
    for i in range(n):
        print(i - 1, lyrics)
def song(n):
    print(f"{n} bottles of beer on the wall,")
    print(f"{n} bottles of beer.")
    print("Take one down, pass it around,")
    print(f"{n - 1} bottles of beer on the wall.")
for i in range(99, 0, -1):
    song(i)