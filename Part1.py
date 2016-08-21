# Code For Interview Part 1 #

# 1 Longest chain

# 给一个字符串数组, 以任意一个单词开始，删除一个字母 ，如果形成的新字符串还在数组的单词堆里面，则是合法的， chain长度增加1.然后继续往下删，每删一个则长度增加1. 举些例子吧：(a, abcd, bcd, abd, cd, c)：
# abcd 删除一个字母可以变成 bcd ， abd， acd，abc。但是只有bcd， acd 可以往下走，所以下面只要考虑这两个。 bcd 可以变成cd 再变成c。 但是abd删除一个单词不能变成数组的一个单词。所以停止。

def deleteOneLetter(strOrig):
    result = []
    for i in strOrig:
        result.append(strOrig[0:strOrig.index(i)] + strOrig[strOrig.index(i)+1:len(strOrig)])
    return result


testExample = ['abcd','bcd','a','bd','abc']

for run in testExample:
    count = 1
    while count
    run_Result = deleteOneLetter(run)
    for check in run_Result:
        for check2 in testExample:
            if check == check2:
                count = count + 1
