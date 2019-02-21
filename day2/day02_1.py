# i = 1
# while i <= 5:
#     j = 1
#     while j <= i:
#         print("*", end=" ")
#         j += 1
#     print("")
#     i += 1

i = 1
while i <= 9:
    j = 1
    while j <= i:
        # print(int(i) + "*" + int(j) + "=" + int(i) * int(j))
        print(i, "*", j, "=", i*j,  end="\t")
        j += 1
    print(" ")
    i += 1
print(-5//4)