import numpy as np
import matplotlib.pyplot as plt

def random_walk_displacement(num_steps, num_simulations):
    """
    模拟随机行走并返回每次模拟的最终位移

    参数:
    num_steps (int): 随机行走的步数
    num_simulations (int): 模拟的次数

    返回:
    numpy.ndarray: 形状为(2, num_simulations)的数组，表示每次模拟的最终位移
    """
    # TODO: 检查输入参数的有效性
    
    # TODO: 实现随机行走算法
    # 提示：
    # 1. 使用 np.random.choice 生成随机步长 ([-1, 1])
    # 2. 生成形状为 (2, num_simulations, num_steps) 的数组
    # 3. 对步数维度求和得到最终位移
    
    # 检查输入参数的有效性
    if num_steps <= 0 or num_simulations <= 0:
        raise ValueError("num_steps和num_simulations必须为正整数")
    
    # 实现随机行走算法
    # 生成随机步长 ([-1, 1])，形状为 (2, num_simulations, num_steps)
    steps = np.random.choice([-1, 1], size=(2, num_simulations, num_steps))
    
    # 对步数维度求和得到最终位移
    final_displacements = np.sum(steps, axis=2)
    
    return final_displacements

def plot_displacement_distribution(final_displacements, bins=30):
    """
    绘制位移分布直方图

    参数:
    final_displacements (list): 包含每次模拟最终位移的列表
    bins (int): 直方图的组数
    """
    # TODO: 实现位移分布的直方图绘制
    # 1. 计算每次模拟的最终位移
    # 2. 使用plt.hist绘制直方图
    # 3. 添加标题和标签
    # 计算每次模拟的最终位移大小
    r = np.sqrt(final_displacements[0]**2 + final_displacements[1]**2)
    
    # 绘制直方图
    plt.figure(figsize=(8, 6))
    plt.hist(r, bins=bins, density=True, alpha=0.7, color='blue', edgecolor='black')
    
    # 添加标题和标签
    plt.title('Final Displacement Distribution')
    plt.xlabel('Displacement (r)')
    plt.ylabel('Probability Density')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.show()

def plot_displacement_square_distribution(final_displacements, bins=30):
    """
    绘制位移平方分布直方图

    参数:
    final_displacements (list): 包含每次模拟最终位移的列表
    bins (int): 直方图的组数
    """
    # TODO: 实现位移平方分布的直方图绘制
    # 1. 计算位移平方
    # 2. 使用plt.hist绘制直方图
    # 3. 添加标题和标签
    # 计算位移平方
    r_squared = final_displacements[0]**2 + final_displacements[1]**2
    
    # 绘制直方图
    plt.figure(figsize=(8, 6))
    plt.hist(r_squared, bins=bins, density=True, alpha=0.7, color='green', edgecolor='black')
    
    # 添加标题和标签
    plt.title('Squared Displacement Distribution')
    plt.xlabel('Squared Displacement (r²)')
    plt.ylabel('Probability Density')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.show()

if __name__ == "__main__":
    # 可调整的参数
    num_steps = 1000  # 随机行走的步数
    num_simulations = 1000  # 模拟的次数
    bins = 30  # 直方图的组数

    # TODO: 完成主程序逻辑
    # 1. 调用random_walk_displacement获取模拟结果
    # 2. 绘制位移分布直方图
    # 3. 绘制位移平方分布直方图
    # 主程序逻辑
    # 1. 调用random_walk_displacement获取模拟结果
    final_displacements = random_walk_displacement(num_steps, num_simulations)
    
    # 2. 绘制位移分布直方图
    plot_displacement_distribution(final_displacements, bins)
    
    # 3. 绘制位移平方分布直方图
    plot_displacement_square_distribution(final_displacements, bins)
