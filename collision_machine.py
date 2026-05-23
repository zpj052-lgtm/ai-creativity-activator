import os
import json
import time
import argparse
from agents import LawFinder, ProblemCollider, IdeaJudge

def main():
    parser = argparse.ArgumentParser(description="Market Collision Machine - 跨界量化灵感生成器")
    parser.add_argument("--iterations", type=int, default=100, help="运行循环次数 (默认: 100)")
    parser.add_argument("--problem", type=str, default="如何识别并利用股票市场的‘情绪反转’？", help="目标难题内容")
    parser.add_argument("--output", type=str, default="results", help="结果保存目录")
    
    args = parser.parse_args()

    finder = LawFinder()
    collider = ProblemCollider()
    judge = IdeaJudge()

    problem = args.problem
    output_dir = args.output
    iterations = args.iterations
    
    print(f"🚀 开始运行碰撞机器")
    print(f"🎯 目标问题: {problem}")
    print(f"🔄 计划循环: {iterations} 次")
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    used_laws = []
    
    for i in range(1, iterations + 1):
        try:
            print(f"\n--- 正在进行第 {i}/{iterations} 次碰撞 ---")
            
            # 1. 寻找规律
            law = finder.find_law(used_laws=used_laws[-10:])
            used_laws.append(law.split('\n')[0])
            print(f"🔍 找到规律: {law.split('\n')[0]}")
            
            # 2. 碰撞点子
            spark = collider.collide(law, problem)
            print("💥 碰撞产生火花...")
            
            # 3. 裁判评价
            score = judge.judge(spark)
            print(f"⚖️ 评价结果: {score.split('\n')[0]}")
            
            # 保存结果
            result = {
                "iteration": i,
                "problem": problem,
                "law": law,
                "spark": spark,
                "judge": score
            }
            
            with open(f"{output_dir}/collision_{i}.json", "w", encoding="utf-8") as f:
                json.dump(result, f, ensure_ascii=False, indent=4)
                
            if i % 10 == 0:
                print(f"\n📊 已完成 {i} 次，进度 {int(i/iterations*100)}%")
                
        except Exception as e:
            print(f"❌ 第 {i} 次循环出错: {e}")
            time.sleep(5)

    print(f"\n✅ 所有 {iterations} 次碰撞已完成！结果保存在 {output_dir} 目录下。")

if __name__ == "__main__":
    main()
