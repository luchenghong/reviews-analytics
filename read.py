#read

data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0:
            print(len(data))
print('档案读取完毕，共有', len(data),'笔资料')
print(data[0])

sum_len = 0
for review in data:
    sum_len += len(review)
print('平均长度为', sum_len/len(data))

new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('一共有', len(new), '笔留言长度小于100')
print(new[0])
print(new[1])


good_list = []
for d in data:
    if 'good' in d:
        good_list.append(d)
print('一共有', len(good_list), '笔留言含 有good')
print(good_list[0])

# good = [d for d in data if 'good' in d]


# 文字计数

wc = {} # word_count
for d in data:
    words = d.split() # 预设值为' '
    for word in words:
        if word in wc:
            wc[word] = wc[word] + 1
        else:
            wc[word] = 1 # 新增新的key进wc字典
for word in wc:
    if wc[word] > 1000000:
        print(word, wc[word])
print(len(wc))
print(wc['jack'])


while True:
    word = input('请问你想要查什么字')
    if word == 'q':
        print(word, '出现过多少次：', wc[word])
        word = input('请问你想要退出吗（y/n）')
        if word == 'y':
            break
        else:
            continue
    if word in wc:
        print(word, '出现过多少次：', wc[word])
    else:
        print('这个字没有出现过')
print('感谢本次使用')



