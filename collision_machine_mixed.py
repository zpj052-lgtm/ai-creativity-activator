import os
import json
import time
import argparse
import random
from agents import LawFinder, ProblemCollider, IdeaJudge

def main():
    parser = argparse.ArgumentParser(description="Multi-Source Collision Machine - 全能灵感实验室")
    parser.add_argument("--iterations", type=int, default=10, help="运行循环次数 (默认: 10)")
    parser.add_argument("--problem", type=str, default="如何构思一个既符合逻辑又出人意料、具有哲学深度且能引发社会共鸣的小说情节或商业点子？", help="目标难题")
    parser.add_argument("--output", type=str, default="results_mixed", help="结果保存目录")
    
    args = parser.parse_args()

    finder = LawFinder()
    collider = ProblemCollider()
    judge = IdeaJudge()

    problem = args.problem
    output_dir = args.output
    iterations = args.iterations
    
    # 支持的来源库
    domains = ["science", "humanities", "news", "myth", "joke", "comment"]
    
    print(f"🚀 开始运行全领域碰撞机器")
    print(f"🎯 目标问题: {problem}")
    print(f"📚 来源库: {', '.join(domains)}")
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    used_concepts = []
    
    for i in range(1, iterations + 1):
        try:
            # 随机选择一个来源领域
            domain = random.choice(domains)
            print(f"\n--- 正在进行第 {i}/{iterations} 次碰撞 [来源: {domain}] ---")
            
            # 1. 寻找核心概念/规律/案例
            concept = finder.find_law(domain=domain, used_laws=used_concepts[-10:])
            used_concepts.append(concept.split('\n')[0])
            print(f"🔍 找到核心素材: {concept.split('\n')[0]}")
            
            # 2. 碰撞点子
            spark = collider.collide(concept, problem)
            print("💥 碰撞产生火花...")
            
            # 3. 裁判评价
            score = judge.judge(spark)
            print(f"⚖️ 评价结果: {score.split('\n')[0]}")
            
            # 保存结果
            result = {
                "iteration": i,
                "domain": domain,
                "problem": problem,
                "concept": concept,
                "spark": spark,
                "judge": score
            }
            
            with open(f"{output_dir}/mixed_collision_{i}.json", "w", encoding="utf-8") as f:
                json.dump(result, f, ensure_ascii=False, indent=4)
                
        except Exception as e:
            print(f"❌ 第 {i} 次循环出错: {e}")
            time.sleep(5)

    print(f"\n✅ 全领域碰撞任务完成！结果保存在 {output_dir} 目录下。")

if __name__ == "__main__":
    main()
