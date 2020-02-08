def grouping(string):
    lists = []
    lists = [
          "字母", [letter for letter in string if ('A' <= letter <= 'Z' or 'a' <= letter <= 'z')],
          "数字", [int(num) for num in string if '0' <= num <= '9'],
          "符号", [symbol for symbol in string if symbol.isalnum() == 0]]
    return lists


while 1:
    lists0 = input("请输入需要分组的字符串：\n")
    List = grouping(lists0)
    print("分组结果如下:\n")
    for i in range(1, 6, 2):
        print(List[i - 1], "\n\n", List[i], "\n\n")
