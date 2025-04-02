import numpy as np
import matplotlib.pyplot as plt

def random_walk_finals(num_steps=1000, num_walks=1000):
    """生成多个二维随机游走的终点位置
    
    通过模拟多次随机游走，每次在x和y方向上随机选择±1移动，
    计算所有随机游走的终点坐标。

    参数:
        num_steps (int, optional): 每次随机游走的步数. 默认值为1000
        num_walks (int, optional): 随机游走的次数. 默认值为1000
        
    返回:
        tuple: 包含两个numpy数组的元组 (x_finals, y_finals)
            - x_finals: 所有随机游走终点的x坐标数组
            - y_finals: 所有随机游走终点的y坐标数组
    """
    # TODO: 实现随机游走算法
    # 提示：
    # 1. 使用np.zeros初始化数组
    # 2. 使用np.random.choice生成随机步长
    # 3. 使用np.sum计算总位移
    x_finals = np.zeros(num_walks)
    y_finals = np.zeros(num_walks)
    for i in range(num_walks):
        x_finals[i] = np.sum(np.random.choice([-1,1],num_steps))
        y_finals[i] = np.sum(np.random.choice([-1,1],num_steps))
    return (x_finals,y_finals)
    


def calculate_mean_square_displacement():
    """计算不同步数下的均方位移
    
    对于预设的步数序列[1000, 2000, 3000, 4000]，分别进行多次随机游走模拟，
    计算每种步数下的均方位移。每次模拟默认进行1000次随机游走取平均。
    
    返回:
        tuple: 包含两个numpy数组的元组 (steps, msd)
            - steps: 步数数组 [1000, 2000, 3000, 4000]
            - msd: 对应的均方位移数组
    """
    # TODO: 实现均方位移计算
    # 提示：
    # 1. 使用random_walk_finals获取终点坐标
    # 2. 计算位移平方和
    # 3. 使用np.mean计算平均值
    steps = np.array([1000, 2000, 3000, 4000])
    msd = []
    
    for i in steps:
        x_finals, y_finals = random_walk_finals(num_steps=i)  # Fixed function name
        ds = x_finals**2 + y_finals**2
        msd.append(np.mean(ds))
    
    return steps, np.array(msd)


def analyze_step_dependence():
    """分析均方位移与步数的关系，并进行最小二乘拟合
    
    返回:
        tuple: (steps, msd, k)
            - steps: 步数数组
            - msd: 对应的均方位移数组
            - k: 拟合得到的比例系数
    """
    # TODO: 实现数据分析
    # 提示：
    # 1. 调用calculate_mean_square_displacement获取数据
    # 2. 使用最小二乘法拟合 msd = k * steps
    # 3. k = Σ(N·msd)/Σ(N²)
    steps, msd = calculate_mean_square_displacement()
    msd = np.array(msd)
    
    # 最小二乘拟合（强制过原点）
    # 理论上 msd = k * steps，k应该接近2
    k = np.sum(steps * msd) / np.sum(steps**2)
    
    return steps, msd, k


if __name__ == "__main__":
    steps, msd, k = analyze_step_dependence()  # 计算不同步数下的均方位移，同时使用最小二乘法进行拟合

    '''绘制实验数据点'''
    plt.figure(figsize=(8, 6))  # 创建一个8×6英寸的图像窗口
    plt.scatter(steps, msd, color='b', label='experimental data') # 使用散点图 (scatter) 绘制实验数据
                                                        # 步数steps与均方位移msd的图像
                                                        # 定点的颜色为蓝色，图例名称为“实验数据”

    '''
    绘制拟合曲线,以steps为横坐标，k*steps为纵坐标，曲线为红色虚线。图例名称为：“拟合:MSD = x *steps”
    其中x是一个接近2的两位小数
    '''
    plt.plot(steps, k * steps, color='r', linestyle='--', label=f'fitting: MSD = {k:.2f} * steps')

    plt.xlabel('steps (N)')  # 设置x轴标签为"步数 (N)"
    plt.ylabel('mean square displacement ⟨r²⟩')  # 设置y轴标签为"均方位移 ⟨r²⟩"
    plt.title('the relationship between the mean displacement and the number of steps')  # 设置图像标题为“均方位移与步数的关系”
    plt.legend()  # 显示图例
    plt.grid(True)  # 添加网格
    plt.show()  # 显示图像
    print(f'拟合得到的比例系数 k ≈ {k:.2f}')  # 输出拟合比例系数k
