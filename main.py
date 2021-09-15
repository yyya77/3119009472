# -*- coding:utf-8 -*-
import math
import jieba
import jieba.analyse
import numpy as np
import time


def getDistance(hashstr1, hashstr2):
    """
        计算两个汉明距离
    """
    length = 0
    for index, char in enumerate(hashstr1):
        if char == hashstr2[index]:
            continue
        else:
            length += 1
    return length


class SimHash(object):
    def simHash(self, content):
        seg = jieba.cut(content)  # 用jieba进行分词、加权
        keyword = jieba.analyse.extract_tags("|".join(seg), topK=300, withWeight=True)
        keyList = []
        for feature, weight in keyword:
            # print('weight: {}'.format(weight))    weight为权重
            weight = int(math.ceil(weight))
            binstr = self.string_hash(feature)
            temp = []
            for c in binstr:
                if c == '1':
                    temp.append(weight)
                else:
                    temp.append(-weight)
            keyList.append(temp)
        listSum = np.sum(np.array(keyList), axis=0)
        # print(listSum)            测试分词代表的权重
        # print(len(listSum))       测试数组总长度
        if not keyList:
            return '00'
        simhash = ''
        for i in listSum:
            if i > 0:
                simhash += '1'
            else:
                simhash += '0'
        return simhash

    @staticmethod
    def string_hash(source):
        x = ord(source[0]) << 7
        m = 1000003
        mask = 2 ** 128 - 1
        for c in source:
            x = ((x * m) ^ ord(c)) & mask
        x ^= len(source)
        x = bin(x).replace('0b', '').zfill(64)[-64:]
        # print('strint_hash: %s, %s'%(source, x))          可测试分出来的词
        return str(x)


def similarity(self):
    """
    求相似率
    """
    result1 = round((1 - self / 64) * 100, 2)
    return result1


def main():
    shash = SimHash()
    try:  # 正常运行
        a = input("输入一篇文章的路径 eg:【.//test//xxx.txt】:")  # 获取原文地址
        f1 = open(a, 'r', encoding='utf-8')
        sen1 = f1.read()
        b = input("输入另外一篇文章的路径 eg:【.//test//xxx.txt】:")  # 获取抄袭文地址
        f2 = open(b, 'r', encoding='utf-8')
        sen2 = f2.read()
        s1 = shash.simHash(sen1)
        s2 = shash.simHash(sen2)
        # print(s1)                                                #打印原文  检验是否录入
        # print(s2)                                                #打印抄袭文 检验是否录入
        dis = getDistance(s1, s2)  # 求汉明距离
        # print('dis: {}'.format(dis))                             #求出汉明距离
        race = similarity(dis)  # 求相似率
        print("相似率为：%.2f%%" % race)
        result = open('.//test//result.txt', 'a+', encoding='utf-8')
        result.write("%s 与%s 两篇文章相似率为：%.2f \n" % (a, b, race))
        print("结果已保存到result.txt")
        '''
        关闭文件
        '''
        f1.close()
        f2.close()
        result.close()
        time.sleep(5)
    except IndexError:  # 参数错误
        print("请输入有内容的文本路径")
        time.sleep(5)
    except FileNotFoundError:  # 路径错误
        print("请输入正确的路径")
        time.sleep(5)




#for j in range(0, 4):         循环四次遍历所有情况求覆盖率
main()