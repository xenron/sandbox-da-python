# -*- coding:utf-8 -*-
__author__ = 'xenron'

# 训练数据，每行前四项代表特征，最后一项代表类别
my_data = [['slashdot', 'USA', 'yes', 18, 'None'],
           ['google', 'France', 'yes', 23, 'Premium'],
           ['digg', 'USA', 'yes', 24, 'Basic'],
           ['kiwitobes', 'France', 'yes', 23, 'Basic'],
           ['google', 'UK', 'no', 21, 'Premium'],
           ['(direct)', 'New Zealand', 'no', 12, 'None'],
           ['(direct)', 'UK', 'no', 21, 'Basic'],
           ['google', 'USA', 'no', 24, 'Premium'],
           ['slashdot', 'France', 'yes', 19, 'None'],
           ['digg', 'USA', 'no', 18, 'None'],
           ['google', 'UK', 'no', 18, 'None'],
           ['kiwitobes', 'UK', 'no', 19, 'None'],
           ['digg', 'New Zealand', 'yes', 12, 'Basic'],
           ['slashdot', 'UK', 'no', 21, 'None'],
           ['google', 'UK', 'yes', 18, 'Basic'],
           ['kiwitobes', 'France', 'yes', 19, 'Basic']]

# 决策树的节点结构


class decisionnode:
    # 决策树节点初始化
    def __init__(self, col=-1, value=None, results=None, tb=None, fb=None):
        self.col = col   # 代表该节点用训练数据的哪一列作为判断条件
        self.value = value   # 表示col判断条件为value时为真，不为value为假，以此划分节点
        self.results = results  # 表示某一节点中各种类别的字典。除叶节点外，其余节点该项都未None
        self.tb = tb  # 当value为真时的子树
        self.fb = fb  # 当value为假时的子树


# 拆分数据集合，rows为父节点所有的数据，column代表根据第column的判断条件拆分,等于value则为真，否则为假
def divideset(rows, column, value):
    set1, set2 = [], []
    # 如果是数值型数据，则以大于小于拆分
    if isinstance(value, int) or isinstance(value, float):
        for row in rows:
            if row[column] >= value:
                set1.append(row)
            else:
                set2.append(row)
    # 如果是标称数据，则以等于或不等于进行拆分
    else:
        for row in rows:
            if row[column] == value:
                set1.append(row)
            else:
                set2.append(row)
    return (set1, set2)


# 待统计的数据集rows，返回一个字典，键为类别，值为该类别的数据个数
# 返回的字典用于下一步计算数据的混杂程度
def uniquecounts(rows):
    results = {}
    for row in rows:
        results.setdefault(row[len(row) - 1], 0)
        results[row[len(row) - 1]] += 1
    return results


# 计算rows中不同类别的 熵 不纯度
# 熵为0时表示纯度很高，只有一种类别。熵值越高，表明混杂程度越高
def entropy(rows):
    from math import log
    log2 = lambda x: log(x) / log(2)
    results = uniquecounts(rows)
    # 此处计算开始时的熵值
    ent = 0.0
    for r in results.keys():
        p = float(results[r]) / len(rows)
        ent -= p * log2(p)
    return ent


# 以递归方式构造决策树
def buildtree(rows, scoref=entropy):
    if len(rows) == 0:
        return decisionnode()

    # 计算信息增益，从而确定划分属性，信息增益为父节点的熵值减去两个子节点熵值的加权平均和
    # 信息增益越大，表明选择该属性作为划分越好
    best_gain = 0.0
    best_criteria = None
    best_sets = None

    column_count = len(rows[0]) - 1
    # 循环列，循环判定条件
    for col in range(column_count):
        # 统计该判定条件所有的value
        values = []
        for row in rows:
            if row[col] not in values:
                values.append(row[col])
        # 父节点的熵
        e1 = scoref(rows)
        for value in values:
            set1, set2 = divideset(rows, col, value)
            e2 = scoref(set1)
            e3 = scoref(set2)
            p = float(len(set1)) / float(len(rows))
            gain = e1 - p * e2 - (1 - p) * e3
            # 记录信息增益最高的划分条件
            if best_gain < gain:
                best_gain = gain
                best_criteria = (col, value)
                best_sets = (set1, set2)

    # 创建子分支
    if best_gain > 0:
        trueBranch = buildtree(best_sets[0])
        falseBranch = buildtree(best_sets[1])  # 递归继续划分子节点
        return decisionnode(col=best_criteria[0], value=best_criteria[1], results=None,
                            tb=trueBranch, fb=falseBranch)
    # 信息增益为0或负数，表明应该停止分割，该节点为叶节点，叶节点的results不为空
    else:
        return decisionnode(results=uniquecounts(rows))


# 将建立的决策树以文本方式打印输出
def printtree(tree, indent=''):
    # 这是一个叶节点吗
    if tree.results is not None:
        print str(tree.results)
    else:
        # 打印判断条件
        print str(tree.col) + ':' + str(tree.value) + '? '
        # 打印分支
        print indent + 'T->',
        printtree(tree.tb, indent+'  ')
        print indent + 'F->',
        printtree(tree.fb, indent+'  ')


# 对新观测的数据进行分类
def classify(observation, tree):
    # 如果不是叶节点
    if tree.results is None:
        if isinstance(tree.value, int) or isinstance(tree.value, float):
            # 大于
            if observation[tree.col] >= tree.value:
                return classify(observation, tree.tb)
            else:
                return classify(observation, tree.fb)
        else:
            if observation[tree.col] == tree.value:
                return classify(observation, tree.tb)
            else:
                return classify(observation, tree.fb)
    else:
        return tree.results


# 剪枝，剪枝的过程就是对具有相同父节点的两个叶节点进行检查，判断如果将其合并，熵的增加量是否会小于某一
# 阈值，如果小于，则将这两个叶节点合并成一个节点，否则结束
def prune(tree, mingain):
    # 如果分支不是叶节点，则对其进行剪枝操作
    if tree.tb.results is None:
        prune(tree.tb, mingain)  # 向下递归，直到到达叶节点为止
    if tree.fb.results is None:
        prune(tree.fb, mingain)  # 向下递归，知道到达叶节点为止

    # 如果两个子分支都是叶节点，则考察能否进行剪枝
    if tree.tb.results is not None and tree.fb.results is not None:
        tb, fb = [], []
        for v, c in tree.tb.results.items():
            tb += [[v]] * c
        for v, c in tree.fb.results.items():
            fb += [[v]] * c

        # 计算合并后熵的减少情况
        delta = entropy(tb + fb) - (entropy(tb) + entropy(fb))/2
        if delta < mingain:
            tree.tb, tree.fb = None, None
            tree.results = uniquecounts(tb + fb)


if __name__ == '__main__':
    """
    # 测试函数divideset
    set1, set2 = divideset(my_data, 2, 'yes')
    print set1[:]
    print set2[:]
    """
    # 测试uniquecounts
    """
    results = uniquecounts(my_data)
    for key, value in results.items():
        print key, value
    """
    """
    e = entropy(my_data)
    print e
    """

    # 建立决策树
    tree = buildtree(my_data)
    # 打印输出决策树
    #printtree(tree)
    # 预测
    #res = classify(['(direct)', 'USA', 'yes', 5], tree)
    #print "结果: ", res.items()[:]
    # 剪枝
    prune(tree, 1.0)
    printtree(tree)