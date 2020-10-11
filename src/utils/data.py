import numpy as np

def explore_data(Y, n_cls):
    class_grp = { x:0 for x in range(0,n_cls) }
    total_elems = 0

    for cls in Y:
        class_grp[cls] += 1
        total_elems += 1

    for cls in class_grp:
        print(f'class: {cls} | {class_grp[cls]} ({(class_grp[cls] / total_elems * 100):.2f}%) instances')
    print(f'Total number of instances: {total_elems}')

def fold_data(data, k=10):
    np.random.shuffle(data)
    total_elems = len(data)
    fold_size = total_elems // k
    res = []
    for i in range(0, total_elems, fold_size):
        if (i//fold_size) < k:
            res.append(data[i:i+fold_size])
        else:
            res.append(data[i:])
            break
    return res

def load_dataset(filename,dtype=np.float64):
    raw_data = np.loadtxt(filename,dtype=dtype)
    x_data = [e[:-1] for e in raw_data]
    y_data = [e[-1] for e in raw_data]
    return x_data,y_data

def normalization(data, lower_bound=0, higher_bound=1):
    current_min = np.min(data)
    current_max = np.max(data)
    return np.divide(
        (
            (data - current_min) * (higher_bound - lower_bound)
        ), 
        (
            current_max - current_min
        )
    )

def one_hot(y, n_cls):
    cls = []
    for i in y:
        temp = np.zeros(n_cls,dtype=np.int64)
        temp[i] = 1
        cls.append(temp)
    return np.array(cls)

