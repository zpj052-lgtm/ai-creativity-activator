from openai import OpenAI
from config import DEEPSEEK_API_KEY, DEEPSEEK_BASE_URL, MODEL_NAME

class BaseAgent:
    def __init__(self):
        self.client = OpenAI(api_key=DEEPSEEK_API_KEY, base_url=DEEPSEEK_BASE_URL)

    def ask(self, system_prompt, user_prompt):
        response = self.client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            stream=False
        )
        return response.choices[0].message.content

class LawFinder(BaseAgent):
    def find_law(self, domain="science", used_laws=None):
        prompts = {
            "science": {
                "system": "你是一个博学的科学家。你需要提供一个来自物理学、生物学、化学或自然界的底层规律、现象或原理。这个规律必须是具体的、可解释的。",
                "user": "请提供一个新的自然规律。如果是关于流体力学、热力学、生物进化、电磁学等领域的更佳。请给出规律名称和简短描述。"
            },
            "humanities": {
                "system": "你是一个洞察深刻的人文精神方案专家。你需要提供一个来自心理学、行为经济学、社会学、传播学或管理学的底层规律、效应或实验结论。这个规律必须能揭示人性、群体行为或商业竞争的本质。",
                "user": "请提供一个新的社会科学/人文学科规律。例如关于锚定效应、破窗效应、幸存者偏差、马太效应、非零和博弈等领域的规律。请给出规律名称和简短描述。"
            },
            "news": {
                "system": "你是一个敏锐的社会观察家。你需要提供一个最近或经典的“社会新闻”或“热点事件”，并总结其背后的社会心理或冲突核心。",
                "user": "请提供一个具有戏剧性或思考价值的社会新闻案例，并简述其中矛盾冲突的点。"
            },
            "myth": {
                "system": "你是一个博学的神话学家和民俗专家。你需要提供一个世界各地的“神话传说”或“民间故事”，并提炼出其象征意义或循环原型。",
                "user": "请提供一个神话传说故事，并分析其核心象征逻辑。"
            },
            "joke": {
                "system": "你是一个幽默大师和脱口秀编剧。你需要提供一个结构精妙的“笑话”或“梗”，并分析其背后的反转逻辑或荒诞核心。",
                "user": "请提供一个具有深刻底蕴或荒诞感的笑话，并拆解其笑点背后的逻辑反转。"
            },
            "comment": {
                "system": "你是一个互联网深潜者。你需要提供一个网络上的“高赞评价”或“神评论”，并分析其为何能引起强烈共鸣的心理机制。",
                "user": "请提供一个犀利、幽默或富有哲理的互联网高赞评论，并简述其共鸣核心。"
            }
        }
        
        config = prompts.get(domain, prompts["science"])
        system_prompt = config["system"]
        user_prompt = config["user"]
            
        if used_laws:
            user_prompt += f"\n已经使用过的案例/规律包括: {', '.join(used_laws)}。请不要重复。"
        
        return self.ask(system_prompt, user_prompt)

class ProblemCollider(BaseAgent):
    def collide(self, law, problem):
        system_prompt = """你是一个跨界创新专家。你的任务是将一个“自然规律”强行应用到解决一个“股票市场问题”上。
不要流于表面，要深入探讨规律的本质逻辑如何迁移。
输出格式要求：
1. 规律核心：(简述规律及其核心逻辑)
2. 碰撞火花：(将规律应用到股票问题的具体点子)
3. 实施建议：(如何把这个点子变成可操作的量化策略或观察指标)"""
        user_prompt = f"规律：{law}\n股票市场问题：{problem}"
        return self.ask(system_prompt, user_prompt)

class IdeaJudge(BaseAgent):
    def judge(self, idea):
        system_prompt = """你是一个严苛的量化投资总监和风控专家。
你需要对产生的“碰撞点子”进行打分（0-10分）并给出简短评论。
打分维度：
- 逻辑严密性 (Logic)
- 创新性 (Innovation)
- 实战潜力 (Potential)
请给出最终得分和点评。"""
        user_prompt = f"请评估以下点子：\n{idea}"
        return self.ask(system_prompt, user_prompt)
