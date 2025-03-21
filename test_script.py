import pytest
import numpy as np
from script import create_and_sum_array

def test_create_and_sum_array():
    """
    create_and_sum_array 関数のテスト
    """
    # 関数を実行して結果を取得
    arr, total = create_and_sum_array()
    
    # 合計値を確認
    expected_total = 6
    assert total == expected_total, f"Expected total {expected_total}, but got {total}"