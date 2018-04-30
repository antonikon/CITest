import my_module

def test_sum_nums():
	assert my_module.sum_nums(2, 3) == 5
	assert my_module.sum_nums(3, 3) == 6

def test_mul_nums():
	assert my_module.mul_nums(2, 5) == 10
	assert my_module.mul_nums(10, 10) == 100

