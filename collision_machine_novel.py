import os
import json
import time
import argparse
import random
from agents import LawFinder, ProblemCollider, IdeaJudge

def main():
    parser = argparse.ArgumentParser(description="Novel Collision Machine - 创意文学碰撞机")
    parser.add_argument("--iterations", type=int, default=5, help="运行循环次数 (默认: 5)")
    parser.add_argument("--problem", type=str, default="如何构思一个基于硬核科学规律、具有哲学深度且出人意料的小说情节反转？", help="目标文学难题")
    parser.add_argument("--output", type=str, default="results_novel", help="结果保存目录")
    
    args = parser.parse_args()

    finder = LawFinder()
    collider = ProblemCollider()
    judge = IdeaJudge()

    problem = args.problem
    output_dir = args.output
    iterations = args.iterations
    
    print(f"🚀 开始运行小说情节碰撞机器")
    print(f"✍️ 目标难题: {problem}")
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    used_laws = []
    
    for i in range(1, iterations + 1):
        try:
            # 小说领域使用指定的丰富来源库
            novel_domains = ["news", "myth", "joke", "comment", "science", "cases"]
            domain = random.choice(novel_domains)
            print(f"\n--- 正在进行第 {i}/{iterations} 次文学碰撞 [场景: {domain}] ---")
            
            law = finder.find_law(domain=domain, used_laws=used_laws[-10:])
            used_laws.append(law.split('\n')[0])
            print(f"🔍 找到硬核规律: {law.split('\n')[0]}")
            
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
            
            with open(f"{output_dir}/novel_collision_{i}.json", "w", encoding="utf-8") as f:
                json.dump(result, f, ensure_ascii=False, indent=4)
                
        except Exception as e:
            print(f"❌ 第 {i} 次循环出错: {e}")
            time.sleep(5)

    print(f"\n✅ 小说碰撞任务完成！结果保存在 {output_dir} 目录下。")

if __name__ == "__main__":
    main()
