import matplotlib.pyplot as plt
from datetime import datetime

class PressureForge:
    def __init__(self):
        self.stress_log = []
        
    def log_stress(self, category, level, note=""):
        """记录压力事件
        Args:
            category: 法律/经济/职业/健康 
            level: 1-10
            note: 触发原因
        """
        entry = {
            "timestamp": datetime.now().isoformat(),
            "category": category,
            "level": int(level),
            "note": note
        }
        self.stress_log.append(entry)
        self._generate_plot()
        
    def _generate_plot(self):
        """生成动态压力图谱"""
        categories = ['法律', '经济', '职业', '健康']
        avg_levels = [
            sum([e['level'] for e in self.stress_log if e['category']=='法律'])/(len(self.stress_log) or 1),
            sum([e['level'] for e in self.stress_log if e['category']=='经济'])/(len(self.stress_log) or 1),
            sum([e['level'] for e in self.stress_log if e['category']=='职业'])/(len(self.stress_log) or 1),
            sum([e['level'] for e in self.stress_log if e['category']=='健康'])/(len(self.stress_log) or 1)
        ]
        
        plt.figure(figsize=(10,6))
        plt.bar(categories, avg_levels, color=['#FF6B6B','#4ECDC4','#45B7D1','#96CEB4'])
        plt.title(f'Pressure Forge - {datetime.now().strftime("%Y-%m-%d")}')
        plt.ylim(0,10)
        plt.savefig('stress_profile.png')
        print("压力图谱已更新 → stress_profile.png")

if __name__ == "__main__":
    pf = PressureForge()
    pf.log_stress('法律', 8, '社保补缴纠纷')
    pf.log_stress('经济', 9, '投资亏损')
    pf.log_stress('职业', 7, '就业不确定性')
