import numpy as np
import matplotlib.pyplot as plt

def random_walk_finals(num_steps, num_walks):
    """生成多个二维随机游走的终点位置
    
    通过模拟多次随机游走，每次在x和y方向上随机选择±1移动，
    计算所有随机游走的终点坐标。每个随机游走都从原点(0,0)开始。

    参数:
        num_steps (int): 每次随机游走的步数
        num_walks (int): 随机游走的次数
        
    返回:
        tuple: 包含两个numpy数组的元组 (x_finals, y_finals)
            - x_finals: 所有随机游走终点的x坐标数组，长度为num_walks
            - y_finals: 所有随机游走终点的y坐标数组，长度为num_walks
            
    示例:
        >>> x_finals, y_finals = random_walk_finals(1000, 100)
        >>> print(f"第一个终点坐标: ({x_finals[0]}, {y_finals[0]})")
    """
    x_finals = np.zeros(num_walks)
    y_finals = np.zeros(num_walks)
    for i in range(num_walks):
        x_finals[i] = np.sum(np.random.choice([-1,1],num_steps))
        y_finals[i] = np.sum(np.random.choice([-1,1],num_steps))
    return (x_finals,y_finals)

def plot_endpoints_distribution(endpoints):
    """绘制二维随机游走终点的空间分布散点图
    
    将多次随机游走的终点在二维平面上可视化，观察其空间分布特征。
    图形包含所有终点的散点图，并保持x和y轴的比例相同。

    参数:
        endpoints: 包含x和y坐标的元组 (x_coords, y_coords)
            - x_coords: numpy数组，所有终点的x坐标
            - y_coords: numpy数组，所有终点的y坐标
            
    示例:
        >>> endpoints = random_walk_finals(1000, 1000)
        >>> plot_endpoints_distribution(endpoints)
        >>> plt.show()
    """
    x_coords, y_coords = endpoints  # 直接解包坐标
    plt.scatter(x_coords, y_coords, alpha=0.5)
    plt.axis('equal')
    plt.title('Endpoint Distribution Scatter Plot')
    plt.xlabel('X')
    plt.ylabel('Y')

if __name__ == "__main__":
    np.random.seed(42)  # 设置随机种子以保证可重复性
    
    # 生成数据
    endpoints = random_walk_finals(1000, 1000)

    # 创建图形
    plt.figure(figsize=(12, 5))
    
    # 绘制终点分布
    plt.subplot(121)
    plot_endpoints_distribution(endpoints)
    
    # 分析x坐标分布
    plt.subplot(122)
    analyze_x_distribution(endpoints)
    
    plt.tight_layout()
    plt.show()
