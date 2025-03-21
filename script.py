import numpy as np

def create_and_sum_array():
    """
    np.int32 を使用して NumPy 配列を作成し、その要素を足し合わせる関数
    """
    arr = np.array([1, 2, 3], dtype=np.int32)
    total = np.sum(arr)
    return arr, total
  # 修正対象のファイル

if __name__ == "__main__":
    arr, total = create_and_sum_array()
    print("Array:", arr)
    print("Data type:", arr.dtype)
    print("Sum of elements:", total)
    #