import os
import json
import time
import argparse
from agents import LawFinder, ProblemCollider, IdeaJudge

def main():
    parser = argparse.ArgumentParser(description="Trade Collision Machine - 外贸获客灵感生成器")
    parser.add_argument("--iterations", type=int, default=10, help="运行循环次数 (默认: 10)")
    parser.add_argument("--problem", type=str, default="如何识别并捕获那些正处于‘更换供应商临界点’的高质量外贸活跃客户？", help="目标难题内容")
    parser.add_argument("--output", type=str, default="results_trade", help="结果保存目录")
    
    args = parser.parse_args()

    finder = LawFinder()
    collider = ProblemCollider()
    judge = IdeaJudge()

    problem = args.problem
    output_dir = args.output
    iterations = args.iterations
    
    print(f"🚀 开始运行外贸碰撞机器 (人文学科模式)")
    print(f"🎯 目标问题: {problem}")
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    used_laws = []
    
    for i in range(1, iterations + 1):
        try:
            print(f"\n--- 正在进行第 {i}/{iterations} 次外贸碰撞 [来源: humanities] ---")
            
            # 外贸领域固定使用人文、心理与商学规律
            law = finder.find_law(domain="humanities", used_laws=used_laws[-10:])
            used_laws.append(law.split('\n')[0])
            print(f"🔍 找到人文规律: {law.split('\n')[0]}")
            
            # 2. 碰撞点子
            spark = collider.collide(law, problem)
            print("💥 碰撞产生火花...")
            
            # 3. 裁判评价 (评价标准会自动适应问题)
            score = judge.judge(spark)
            print(f"⚖️ 评价结果: {score.split('\n')[0]}")
            
            # 保存结果
            result = {
                "iteration": i,
                "domain": "humanities",
                "problem": problem,
                "law": law,
                "spark": spark,
                "judge": score
            }
            
            with open(f"{output_dir}/trade_collision_{i}.json", "w", encoding="utf-8") as f:
                json.dump(result, f, ensure_ascii=False, indent=4)
                
        except Exception as e:
            print(f"❌ 第 {i} 次循环出错: {e}")
            time.sleep(5)

    print(f"\n✅ 外贸碰撞任务完成！结果保存在 {output_dir} 目录下。")

if __name__ == "__main__":
    main()
