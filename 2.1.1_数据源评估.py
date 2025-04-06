"""
2.1.1 数据源评估与选择

本模块对电影数据进行初步评估，包括：
1. 数据基本信息统计
2. 数据质量评估
3. 数据完整性检查
4. 数据源可靠性分析
"""

import pandas as pd
import numpy as np
import os

class DataSourceEvaluator:
    def __init__(self):
        """初始化数据评估器"""
        try:
            self.data = pd.read_csv('../../电影数据.csv')
            print(f"数据加载成功，共 {len(self.data)} 条记录")
            
            # 创建输出目录
            self.output_dir = '../../分析结果/2.1.1 数据源评估'
            if not os.path.exists(self.output_dir):
                os.makedirs(self.output_dir)
                
        except Exception as e:
            print(f"数据加载错误: {str(e)}")
            raise
    
    def analyze_basic_info(self):
        """分析数据基本信息"""
        basic_info = {
            '总记录数': len(self.data),
            '特征数量': len(self.data.columns),
            '数据类型': self.data.dtypes.to_dict(),
            '内存占用': f"{self.data.memory_usage().sum() / 1024 / 1024:.2f} MB"
        }
        
        return pd.DataFrame([basic_info])
    
    def evaluate_data_quality(self):
        """评估数据质量"""
        quality_stats = pd.DataFrame({
            '缺失值比例': (self.data.isnull().sum() / len(self.data) * 100).round(2),
            '唯一值数量': self.data.nunique(),
            '唯一值比例': (self.data.nunique() / len(self.data) * 100).round(2)
        })
        
        return quality_stats
    
    def check_data_completeness(self):
        """检查数据完整性"""
        completeness = {
            '完整记录数': len(self.data.dropna()),
            '完整记录比例': f"{(len(self.data.dropna()) / len(self.data) * 100):.2f}%",
            '部分缺失记录数': len(self.data) - len(self.data.dropna()),
            '部分缺失比例': f"{((len(self.data) - len(self.data.dropna())) / len(self.data) * 100):.2f}%"
        }
        
        return pd.DataFrame([completeness])
    
    def generate_evaluation_report(self):
        """生成评估报告"""
        try:
            # 1. 基本信息分析
            basic_info = self.analyze_basic_info()
            basic_info.to_csv(f'{self.output_dir}/基本信息统计.csv', index=False, encoding='utf-8-sig')
            
            # 2. 数据质量评估
            quality_stats = self.evaluate_data_quality()
            quality_stats.to_csv(f'{self.output_dir}/数据质量统计.csv', encoding='utf-8-sig')
            
            # 3. 完整性检查
            completeness = self.check_data_completeness()
            completeness.to_csv(f'{self.output_dir}/完整性检查.csv', index=False, encoding='utf-8-sig')
            
            print("\n评估报告生成完成！")
            print(f"结果已保存至: {self.output_dir}")
            
            return {
                'basic_info': basic_info,
                'quality_stats': quality_stats,
                'completeness': completeness
            }
            
        except Exception as e:
            print(f"报告生成错误: {str(e)}")
            raise

def main():
    """主函数"""
    try:
        print("开始数据源评估...")
        
        # 创建评估器
        evaluator = DataSourceEvaluator()
        
        # 生成评估报告
        results = evaluator.generate_evaluation_report()
        
        # 打印关键发现
        print("\n关键发现:")
        print(f"1. 数据集包含 {len(evaluator.data)} 条记录")
        print(f"2. 特征数量: {len(evaluator.data.columns)}")
        print(f"3. 完整记录比例: {results['completeness']['完整记录比例'].values[0]}")
        
    except Exception as e:
        print(f"\n程序执行出错: {str(e)}")
        raise

if __name__ == "__main__":
    main() 