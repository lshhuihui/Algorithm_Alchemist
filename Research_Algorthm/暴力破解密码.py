def brute_force_crack(password, length=6):  # 这里将默认长度改为6
    """
    暴力破解数字密码
    :param password: 正确密码（字符串，如"123456"）
    :param length: 密码长度
    :return: 破解成功的密码及尝试次数
    """
    attempts = 0
    # 遍历所有可能的数字组合（0到10^length - 1），6位密码对应0~999999
    for candidate in range(10 **length):
        # 将数字转换为固定长度的字符串（补前导零，确保6位长度）
        candidate_str = f"{candidate:0{length}d}"
        attempts += 1
        # 每1000次尝试打印一次进度（6位密码共100万次）
        if attempts % 1000 == 0:
            print(f"尝试第{attempts}次：{candidate_str}")
        # 验证候选密码是否正确
        if candidate_str == password:
            return candidate_str, attempts
    return None, attempts  # 理论上不会触发（前提是密码在解空间内）

# 破解6位数字密码"364321"
if __name__ == "__main__":
    target_password = "364321"  # 目标密码为6位
    cracked_pwd, total_attempts = brute_force_crack(target_password)
    print(f"\n破解成功！正确密码是：{cracked_pwd}，共尝试{total_attempts}次")