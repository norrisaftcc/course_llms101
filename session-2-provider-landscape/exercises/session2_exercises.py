"""
Session 2: LLM Provider Landscape - Hands-on Exercises
"""

import time
import json
from typing import Dict, List
import openai
import anthropic
import google.generativeai as genai

class LLMProviderComparison:
    """Compare responses and costs across LLM providers"""
    
    def __init__(self):
        self.providers = {
            "openai": {
                "client": None,
                "model": "gpt-3.5-turbo",
                "input_cost": 0.0005,  # per 1K tokens
                "output_cost": 0.0015  # per 1K tokens
            },
            "anthropic": {
                "client": None,
                "model": "claude-3-haiku-20240307",
                "input_cost": 0.00025,
                "output_cost": 0.00125
            },
            "google": {
                "client": None,
                "model": "gemini-pro",
                "input_cost": 0.00025,
                "output_cost": 0.00125
            }
        }
        
    def setup_providers(self, api_keys: Dict[str, str]):
        """Initialize provider clients with API keys"""
        if "openai" in api_keys:
            openai.api_key = api_keys["openai"]
            self.providers["openai"]["client"] = openai
            
        if "anthropic" in api_keys:
            self.providers["anthropic"]["client"] = anthropic.Client(api_keys["anthropic"])
            
        if "google" in api_keys:
            genai.configure(api_key=api_keys["google"])
            self.providers["google"]["client"] = genai
    
    def compare_responses(self, prompt: str) -> Dict:
        """Compare responses from different providers"""
        results = {}
        
        for provider_name, provider_info in self.providers.items():
            if provider_info["client"] is None:
                continue
                
            start_time = time.time()
            
            try:
                if provider_name == "openai":
                    response = openai.ChatCompletion.create(
                        model=provider_info["model"],
                        messages=[{"role": "user", "content": prompt}]
                    )
                    content = response.choices[0].message.content
                    tokens_used = response.usage.total_tokens
                    
                elif provider_name == "anthropic":
                    response = provider_info["client"].messages.create(
                        model=provider_info["model"],
                        messages=[{"role": "user", "content": prompt}],
                        max_tokens=1000
                    )
                    content = response.content[0].text
                    tokens_used = response.usage.input_tokens + response.usage.output_tokens
                    
                elif provider_name == "google":
                    model = genai.GenerativeModel(provider_info["model"])
                    response = model.generate_content(prompt)
                    content = response.text
                    tokens_used = len(prompt.split()) * 1.3  # Rough estimate
                
                elapsed_time = time.time() - start_time
                
                results[provider_name] = {
                    "response": content,
                    "tokens": tokens_used,
                    "time": elapsed_time,
                    "cost": self.calculate_cost(provider_name, tokens_used)
                }
                
            except Exception as e:
                results[provider_name] = {
                    "error": str(e),
                    "time": time.time() - start_time
                }
        
        return results
    
    def calculate_cost(self, provider: str, tokens: int) -> float:
        """Calculate cost for a given number of tokens"""
        provider_info = self.providers[provider]
        # Simplified calculation assuming 50/50 input/output split
        input_tokens = tokens / 2
        output_tokens = tokens / 2
        
        input_cost = (input_tokens / 1000) * provider_info["input_cost"]
        output_cost = (output_tokens / 1000) * provider_info["output_cost"]
        
        return input_cost + output_cost
    
    def cost_analysis(self, monthly_volume: int) -> Dict:
        """Analyze costs across providers for monthly token volume"""
        analysis = {}
        
        for provider_name, provider_info in self.providers.items():
            monthly_cost = self.calculate_cost(provider_name, monthly_volume)
            analysis[provider_name] = {
                "monthly_cost": monthly_cost,
                "yearly_cost": monthly_cost * 12,
                "cost_per_1k_tokens": monthly_cost / (monthly_volume / 1000)
            }
        
        return analysis


class ProviderEvaluationMatrix:
    """Build a decision matrix for provider selection"""
    
    def __init__(self):
        self.criteria = {
            "cost": {"weight": 0.25, "scores": {}},
            "performance": {"weight": 0.20, "scores": {}},
            "capabilities": {"weight": 0.20, "scores": {}},
            "reliability": {"weight": 0.15, "scores": {}},
            "ecosystem": {"weight": 0.10, "scores": {}},
            "support": {"weight": 0.10, "scores": {}}
        }
        
        self.providers = ["openai", "anthropic", "google", "cohere", "mistral"]
    
    def add_scores(self, provider: str, scores: Dict[str, float]):
        """Add evaluation scores for a provider (0-10 scale)"""
        for criterion, score in scores.items():
            if criterion in self.criteria:
                self.criteria[criterion]["scores"][provider] = score
    
    def calculate_weighted_scores(self) -> Dict[str, float]:
        """Calculate weighted scores for each provider"""
        weighted_scores = {provider: 0.0 for provider in self.providers}
        
        for criterion, info in self.criteria.items():
            weight = info["weight"]
            scores = info["scores"]
            
            for provider in self.providers:
                if provider in scores:
                    weighted_scores[provider] += scores[provider] * weight
        
        return weighted_scores
    
    def get_recommendation(self) -> str:
        """Get the recommended provider based on scores"""
        weighted_scores = self.calculate_weighted_scores()
        return max(weighted_scores, key=weighted_scores.get)
    
    def generate_report(self) -> str:
        """Generate a detailed evaluation report"""
        weighted_scores = self.calculate_weighted_scores()
        recommendation = self.get_recommendation()
        
        report = "# Provider Evaluation Report\n\n"
        report += "## Scores by Criteria\n"
        
        for criterion, info in self.criteria.items():
            report += f"\n### {criterion.title()} (Weight: {info['weight']*100}%)\n"
            for provider, score in info['scores'].items():
                report += f"- {provider}: {score}/10\n"
        
        report += "\n## Final Weighted Scores\n"
        for provider, score in sorted(weighted_scores.items(), 
                                     key=lambda x: x[1], reverse=True):
            report += f"- {provider}: {score:.2f}/10\n"
        
        report += f"\n## Recommendation: **{recommendation}**\n"
        
        return report


# Exercise functions for participants
def exercise_1_basic_comparison():
    """Exercise 1: Basic provider comparison"""
    comparison = LLMProviderComparison()
    
    # TODO: Add your API keys
    api_keys = {
        "openai": "your-openai-key",
        "anthropic": "your-anthropic-key",
        "google": "your-google-key"
    }
    
    comparison.setup_providers(api_keys)
    
    # Test prompt
    prompt = "Explain the concept of recursion in programming in 3 sentences."
    
    results = comparison.compare_responses(prompt)
    
    # Analyze results
    for provider, result in results.items():
        print(f"\n{provider.upper()}:")
        if "error" in result:
            print(f"Error: {result['error']}")
        else:
            print(f"Response: {result['response'][:100]}...")
            print(f"Time: {result['time']:.2f}s")
            print(f"Tokens: {result['tokens']}")
            print(f"Cost: ${result['cost']:.4f}")


def exercise_2_cost_analysis():
    """Exercise 2: Monthly cost analysis"""
    comparison = LLMProviderComparison()
    
    # Estimate monthly token usage
    monthly_tokens = 1_000_000  # 1M tokens per month
    
    cost_analysis = comparison.cost_analysis(monthly_tokens)
    
    print(f"Cost Analysis for {monthly_tokens:,} tokens/month:\n")
    for provider, costs in cost_analysis.items():
        print(f"{provider}:")
        print(f"  Monthly: ${costs['monthly_cost']:.2f}")
        print(f"  Yearly: ${costs['yearly_cost']:.2f}")
        print(f"  Per 1K tokens: ${costs['cost_per_1k_tokens']:.4f}\n")


def exercise_3_build_evaluation_matrix():
    """Exercise 3: Build your own evaluation matrix"""
    matrix = ProviderEvaluationMatrix()
    
    # Example scores (participants should research and add their own)
    matrix.add_scores("openai", {
        "cost": 6,
        "performance": 9,
        "capabilities": 9,
        "reliability": 8,
        "ecosystem": 10,
        "support": 8
    })
    
    matrix.add_scores("anthropic", {
        "cost": 7,
        "performance": 8,
        "capabilities": 8,
        "reliability": 9,
        "ecosystem": 6,
        "support": 7
    })
    
    matrix.add_scores("google", {
        "cost": 8,
        "performance": 7,
        "capabilities": 8,
        "reliability": 8,
        "ecosystem": 9,
        "support": 6
    })
    
    # Generate report
    report = matrix.generate_report()
    print(report)
    
    # Save to file
    with open("provider_evaluation_report.md", "w") as f:
        f.write(report)


if __name__ == "__main__":
    print("Session 2: LLM Provider Landscape Exercises")
    print("==========================================\n")
    
    # Uncomment to run exercises
    # exercise_1_basic_comparison()
    # exercise_2_cost_analysis()
    # exercise_3_build_evaluation_matrix()