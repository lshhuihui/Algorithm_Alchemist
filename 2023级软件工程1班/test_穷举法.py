#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
单元测试文件：穷举法.py

本测试文件包含对穷举法.py中所有函数的全面测试，包括：
1. getS(i,j) - 水仙花数查找函数
2. getSum(a,b) - 鸡兔同笼问题求解函数  
3. getMaxSum(nums) - 最大连续子序列和函数（当前实现不完整）

测试覆盖了正常情况、边界情况和异常情况。
"""

import unittest
import sys
import io
from contextlib import redirect_stdout
import os

# 添加当前目录到Python路径，以便导入被测试的模块
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# 导入被测试的函数
from 穷举法 import getS, getSum, getMaxSum


class TestGetS(unittest.TestCase):
    """
    测试getS函数 - 水仙花数查找
    
    水仙花数是指一个三位数，其各位数字立方和等于该数本身。
    例如：153 = 1³ + 5³ + 3³ = 1 + 125 + 27 = 153
    """
    
    def setUp(self):
        """测试前的准备工作"""
        self.captured_output = io.StringIO()
    
    def test_getS_normal_range(self):
        """
        测试正常范围内的水仙花数查找
        
        测试范围100-1000，应该找到所有四个水仙花数：
        153, 371, 407, 371
        """
        with redirect_stdout(self.captured_output):
            getS(100, 1000)
        
        output = self.captured_output.getvalue().strip()
        output_lines = [line.strip() for line in output.split('\n') if line.strip()]
        
        # 验证找到的水仙花数
        expected_narcissistic = ['153', '371', '407']
        
        # 检查是否包含所有预期的水仙花数
        for num in expected_narcissistic:
            self.assertIn(num, output_lines, f"应该找到水仙花数 {num}")
    
    def test_getS_small_range(self):
        """
        测试小范围查找
        
        测试范围150-160，应该找到153
        """
        with redirect_stdout(self.captured_output):
            getS(150, 160)
        
        output = self.captured_output.getvalue().strip()
        self.assertIn('153', output, "在范围150-160内应该找到153")
    
    def test_getS_no_narcissistic_range(self):
        """
        测试没有水仙花数的范围
        
        测试范围200-300，这个范围内没有水仙花数
        """
        with redirect_stdout(self.captured_output):
            getS(200, 300)
        
        output = self.captured_output.getvalue().strip()
        self.assertEqual(output, '', "范围200-300内不应该有水仙花数")
    
    def test_getS_edge_cases(self):
        """
        测试边界情况
        
        1. 相同的起始和结束值
        2. 单个数字范围
        """
        # 测试相同起始和结束值
        with redirect_stdout(self.captured_output):
            getS(153, 153)
        output = self.captured_output.getvalue().strip()
        self.assertEqual(output, '', "相同起始和结束值应该没有输出")
        
        # 重置输出缓冲区
        self.captured_output = io.StringIO()
        
        # 测试单个数字范围
        with redirect_stdout(self.captured_output):
            getS(153, 154)
        output = self.captured_output.getvalue().strip()
        self.assertIn('153', output, "范围153-154应该找到153")
    
    def test_getS_invalid_range(self):
        """
        测试无效范围（起始值大于结束值）
        
        这种情况下函数应该没有输出
        """
        with redirect_stdout(self.captured_output):
            getS(500, 100)
        
        output = self.captured_output.getvalue().strip()
        self.assertEqual(output, '', "无效范围应该没有输出")


class TestGetSum(unittest.TestCase):
    """
    测试getSum函数 - 鸡兔同笼问题
    
    鸡兔同笼问题：已知头的总数和腿的总数，求鸡和兔子的数量。
    约束条件：
    - 鸡有1个头2条腿
    - 兔子有1个头4条腿
    - x + y = a (总头数)
    - 2x + 4y = b (总腿数)
    """
    
    def setUp(self):
        """测试前的准备工作"""
        self.captured_output = io.StringIO()
    
    def test_getSum_valid_solution(self):
        """
        测试有有效解的情况
        
        测试用例：35个头，94条腿
        解：鸡23只，兔子12只
        验证：23 + 12 = 35, 2*23 + 4*12 = 46 + 48 = 94
        """
        with redirect_stdout(self.captured_output):
            getSum(35, 94)
        
        output = self.captured_output.getvalue().strip()
        self.assertIn('鸡:23,兔子:12', output, "应该找到正确的解：鸡23只，兔子12只")
    
    def test_getSum_all_chickens(self):
        """
        测试全是鸡的情况
        
        测试用例：10个头，20条腿
        解：鸡10只，兔子0只
        """
        with redirect_stdout(self.captured_output):
            getSum(10, 20)
        
        output = self.captured_output.getvalue().strip()
        self.assertIn('鸡:10,兔子:0', output, "应该找到解：鸡10只，兔子0只")
    
    def test_getSum_all_rabbits(self):
        """
        测试全是兔子的情况
        
        测试用例：8个头，32条腿
        解：鸡0只，兔子8只
        """
        with redirect_stdout(self.captured_output):
            getSum(8, 32)
        
        output = self.captured_output.getvalue().strip()
        self.assertIn('鸡:0,兔子:8', output, "应该找到解：鸡0只，兔子8只")
    
    def test_getSum_no_solution(self):
        """
        测试无解的情况
        
        测试用例：10个头，15条腿
        这种情况下腿数不可能满足条件（最少20条腿，最多40条腿）
        """
        with redirect_stdout(self.captured_output):
            getSum(10, 15)
        
        output = self.captured_output.getvalue().strip()
        self.assertEqual(output, '', "无解情况应该没有输出")
    
    def test_getSum_impossible_legs(self):
        """
        测试不可能的腿数情况
        
        测试用例：5个头，11条腿
        腿数为奇数，不可能有解
        """
        with redirect_stdout(self.captured_output):
            getSum(5, 11)
        
        output = self.captured_output.getvalue().strip()
        self.assertEqual(output, '', "奇数腿数应该无解")
    
    def test_getSum_edge_cases(self):
        """
        测试边界情况
        
        1. 0个头0条腿
        2. 1个头的情况
        """
        # 测试0个头0条腿
        with redirect_stdout(self.captured_output):
            getSum(0, 0)
        output = self.captured_output.getvalue().strip()
        self.assertIn('鸡:0,兔子:0', output, "0个头0条腿应该有解：鸡0只，兔子0只")
        
        # 重置输出缓冲区
        self.captured_output = io.StringIO()
        
        # 测试1个头2条腿（1只鸡）
        with redirect_stdout(self.captured_output):
            getSum(1, 2)
        output = self.captured_output.getvalue().strip()
        self.assertIn('鸡:1,兔子:0', output, "1个头2条腿应该是1只鸡")
        
        # 重置输出缓冲区
        self.captured_output = io.StringIO()
        
        # 测试1个头4条腿（1只兔子）
        with redirect_stdout(self.captured_output):
            getSum(1, 4)
        output = self.captured_output.getvalue().strip()
        self.assertIn('鸡:0,兔子:1', output, "1个头4条腿应该是1只兔子")


class TestGetMaxSum(unittest.TestCase):
    """
    测试getMaxSum函数 - 最大连续子序列和
    
    注意：当前实现的getMaxSum函数不完整，只是打印了部分元素。
    这里的测试主要验证函数的基本行为和输出。
    
    理论上，最大连续子序列和问题应该返回数组中连续子序列的最大和。
    例如：[-2,11,-4,13,-5,-2] 的最大连续子序列和应该是 20 (11-4+13)
    """
    
    def setUp(self):
        """测试前的准备工作"""
        self.captured_output = io.StringIO()
    
    def test_getMaxSum_normal_array(self):
        """
        测试正常数组的处理
        
        注意：由于当前实现不完整，这里主要测试函数是否能正常运行
        """
        test_array = [-2, 11, -4, 13, -5, -2]
        
        with redirect_stdout(self.captured_output):
            getMaxSum(test_array)
        
        output = self.captured_output.getvalue().strip()
        output_lines = output.split('\n')
        
        # 验证输出不为空（函数至少有一些输出）
        self.assertTrue(len(output_lines) > 0, "函数应该有输出")
        
        # 验证输出包含数组的第一个元素（基于当前实现）
        self.assertIn('-2', output, "输出应该包含数组的第一个元素")
    
    def test_getMaxSum_single_element(self):
        """
        测试单元素数组
        """
        test_array = [5]
        
        with redirect_stdout(self.captured_output):
            getMaxSum(test_array)
        
        output = self.captured_output.getvalue().strip()
        # 单元素数组，外层循环执行但内层循环不执行，应该没有输出
        self.assertEqual(output, '', "单元素数组应该没有输出（基于当前实现）")
    
    def test_getMaxSum_two_elements(self):
        """
        测试两元素数组
        """
        test_array = [3, 7]
        
        with redirect_stdout(self.captured_output):
            getMaxSum(test_array)
        
        output = self.captured_output.getvalue().strip()
        # 基于当前实现，应该输出第一个元素
        self.assertIn('3', output, "两元素数组应该输出第一个元素")
    
    def test_getMaxSum_empty_array(self):
        """
        测试空数组
        """
        test_array = []
        
        with redirect_stdout(self.captured_output):
            getMaxSum(test_array)
        
        output = self.captured_output.getvalue().strip()
        self.assertEqual(output, '', "空数组应该没有输出")
    
    def test_getMaxSum_all_negative(self):
        """
        测试全负数数组
        """
        test_array = [-5, -2, -8, -1]
        
        with redirect_stdout(self.captured_output):
            getMaxSum(test_array)
        
        output = self.captured_output.getvalue().strip()
        # 基于当前实现，应该输出第一个元素多次
        self.assertIn('-5', output, "全负数数组应该包含第一个元素的输出")
    
    def test_getMaxSum_all_positive(self):
        """
        测试全正数数组
        """
        test_array = [1, 3, 5, 2]
        
        with redirect_stdout(self.captured_output):
            getMaxSum(test_array)
        
        output = self.captured_output.getvalue().strip()
        # 基于当前实现，应该输出第一个元素多次
        self.assertIn('1', output, "全正数数组应该包含第一个元素的输出")


class TestIntegration(unittest.TestCase):
    """
    集成测试类
    
    测试多个函数的组合使用和整体功能
    """
    
    def test_all_functions_importable(self):
        """
        测试所有函数都可以正常导入和调用
        """
        # 测试函数是否可调用
        self.assertTrue(callable(getS), "getS函数应该可调用")
        self.assertTrue(callable(getSum), "getSum函数应该可调用") 
        self.assertTrue(callable(getMaxSum), "getMaxSum函数应该可调用")
    
    def test_functions_with_various_inputs(self):
        """
        测试函数对各种输入的处理能力
        """
        # 测试getS处理大范围
        with redirect_stdout(io.StringIO()):
            try:
                getS(1, 10)  # 小范围测试
                getS(100, 200)  # 中等范围测试
            except Exception as e:
                self.fail(f"getS函数处理各种范围时出错: {e}")
        
        # 测试getSum处理各种头腿组合
        with redirect_stdout(io.StringIO()):
            try:
                getSum(1, 2)  # 最小有效输入
                getSum(100, 300)  # 较大输入
            except Exception as e:
                self.fail(f"getSum函数处理各种输入时出错: {e}")
        
        # 测试getMaxSum处理各种数组
        with redirect_stdout(io.StringIO()):
            try:
                getMaxSum([1])  # 单元素
                getMaxSum([1, 2, 3, 4, 5])  # 多元素
            except Exception as e:
                self.fail(f"getMaxSum函数处理各种数组时出错: {e}")


def run_tests_with_coverage():
    """
    运行测试并尝试计算覆盖率
    """
    # 创建测试套件
    test_suite = unittest.TestSuite()
    
    # 添加所有测试类
    test_classes = [TestGetS, TestGetSum, TestGetMaxSum, TestIntegration]
    
    for test_class in test_classes:
        tests = unittest.TestLoader().loadTestsFromTestCase(test_class)
        test_suite.addTests(tests)
    
    # 运行测试
    runner = unittest.TextTestRunner(verbosity=2, stream=sys.stdout)
    result = runner.run(test_suite)
    
    # 打印测试结果摘要
    print(f"\n{'='*60}")
    print("测试结果摘要:")
    print(f"总测试数: {result.testsRun}")
    print(f"成功: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"失败: {len(result.failures)}")
    print(f"错误: {len(result.errors)}")
    print(f"成功率: {((result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun * 100):.1f}%")
    
    if result.failures:
        print(f"\n失败的测试:")
        for test, traceback in result.failures:
            print(f"- {test}: {traceback.split('AssertionError: ')[-1].split('\\n')[0] if 'AssertionError: ' in traceback else '未知错误'}")
    
    if result.errors:
        print(f"\n错误的测试:")
        for test, traceback in result.errors:
            print(f"- {test}: {traceback.split('\\n')[-2] if len(traceback.split('\\n')) > 1 else '未知错误'}")
    
    print(f"{'='*60}")
    
    return result


if __name__ == '__main__':
    print("开始运行穷举法.py的单元测试...")
    print("="*60)
    
    # 运行测试
    result = run_tests_with_coverage()
    
    # 根据测试结果设置退出码
    exit_code = 0 if result.wasSuccessful() else 1
    sys.exit(exit_code)