from sklearn import datasets
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


def KNN():
    # 通过sklearn自带数据包加载iris数据
    iris = datasets.load_iris()

    # 样本数据和结果分别赋值'x'和'y'
    x = iris.data
    y = iris.target

    # 确认样本与输出维度
    print(x.shape)
    print(y.shape)

    # 创建模型实例
    knn = KNeighborsClassifier(n_neighbors=1)
    print(knn)

    # 训练模型
    knn.fit(x, y)

    # 输出预测结果 [2 0]
    print(knn.predict([[1, 2, 3, 4]]))

    x_test = [[1, 2, 3, 4], [2, 4, 1, 2]]
    knn_5 = KNeighborsClassifier(n_neighbors=5)
    knn_5.fit(x, y)
    y_pred = knn_5.predict(x)
    print(y_pred)
    print(y_pred.shape)
    # 准确率计算
    print(accuracy_score(y, y_pred))

    # [1 0]
    # print(knn_5.predict(x_test))
    # 分离训练集和测试
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4)
    print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)


if __name__ == '__main__':
    KNN()
