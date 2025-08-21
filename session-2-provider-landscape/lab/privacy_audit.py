#!/usr/bin/env python3
"""
Privacy Audit Tool for AI Services
Week 2 Lab - Understanding Your AI Data Trail
"""

import os
import json
import subprocess
from datetime import datetime
from pathlib import Path

class AIPrivacyAuditor:
    """Audit what AI services know about you"""
    
    def __init__(self):
        self.report = {
            "audit_date": datetime.now().isoformat(),
            "findings": [],
            "risks": [],
            "recommendations": []
        }
    
    def check_api_keys(self):
        """Find exposed API keys in environment"""
        print("\n🔍 Checking for API Keys in Environment...")
        
        api_patterns = {
            "OPENAI_API_KEY": "OpenAI (ChatGPT)",
            "ANTHROPIC_API_KEY": "Anthropic (Claude)",
            "GOOGLE_AI_KEY": "Google (Gemini)",
            "HUGGINGFACE_TOKEN": "Hugging Face",
            "COHERE_API_KEY": "Cohere",
            "REPLICATE_API_TOKEN": "Replicate"
        }
        
        found_keys = []
        for key, service in api_patterns.items():
            if os.environ.get(key):
                found_keys.append(service)
                print(f"  ⚠️  Found {service} API key in environment")
                self.report["risks"].append(f"{service} API key exposed in environment")
        
        if not found_keys:
            print("  ✅ No API keys found in environment variables")
        else:
            print(f"\n  Found {len(found_keys)} API key(s) that could be logging your data")
            
        return found_keys
    
    def check_config_files(self):
        """Look for AI service config files"""
        print("\n🔍 Checking for AI Service Config Files...")
        
        home = Path.home()
        config_locations = {
            ".openai": "OpenAI config",
            ".anthropic": "Anthropic config",
            ".config/github-copilot": "GitHub Copilot",
            ".continue": "Continue (AI code assistant)",
            ".cursor": "Cursor preferences",
            ".ollama": "Ollama (local models)"
        }
        
        found_configs = []
        for config_path, service in config_locations.items():
            full_path = home / config_path
            if full_path.exists():
                found_configs.append(service)
                print(f"  📁 Found {service} at {full_path}")
                
                # Check if it's local or cloud
                if "ollama" in service.lower():
                    print(f"     ✅ {service} is LOCAL - your data stays here")
                else:
                    print(f"     ☁️  {service} is CLOUD - your data may be sent externally")
                    self.report["findings"].append(f"{service} configuration found")
        
        return found_configs
    
    def check_browser_storage(self):
        """Check for AI service data in browsers"""
        print("\n🔍 Checking Browser Storage for AI Services...")
        
        services_to_check = [
            ("chat.openai.com", "ChatGPT"),
            ("claude.ai", "Claude"),
            ("gemini.google.com", "Google Gemini"),
            ("bing.com/chat", "Bing Chat"),
            ("perplexity.ai", "Perplexity")
        ]
        
        print("\n  Manual Check Required:")
        print("  Open your browser DevTools (F12) and check:")
        for domain, service in services_to_check:
            print(f"    - {service}: localStorage/cookies for {domain}")
        
        print("\n  What to look for:")
        print("    • Stored conversations")
        print("    • User preferences")
        print("    • Session tokens")
        print("    • Usage analytics")
    
    def analyze_data_retention(self):
        """Show data retention policies"""
        print("\n📊 Data Retention Policies (What They Keep):")
        
        policies = {
            "OpenAI (ChatGPT)": {
                "prompts": "30 days default (can opt out)",
                "conversations": "Indefinitely unless deleted",
                "training": "May use for training unless opted out",
                "api_logs": "30 days"
            },
            "Anthropic (Claude)": {
                "prompts": "90 days default",
                "conversations": "Until you delete",
                "training": "Does NOT use for training (as of 2024)",
                "api_logs": "28 days"
            },
            "Google (Gemini)": {
                "prompts": "18 months default",
                "conversations": "3 years",
                "training": "May use for training",
                "api_logs": "Varies by product"
            },
            "Local (Ollama)": {
                "prompts": "Never leaves your machine",
                "conversations": "Only if you save them",
                "training": "No external training",
                "api_logs": "None sent externally"
            }
        }
        
        for service, policy in policies.items():
            print(f"\n  {service}:")
            for data_type, retention in policy.items():
                icon = "✅" if "never" in retention.lower() or "not" in retention.lower() else "⚠️"
                print(f"    {icon} {data_type}: {retention}")
    
    def calculate_privacy_score(self, found_keys, found_configs):
        """Calculate a privacy risk score"""
        print("\n🎯 Privacy Risk Score:")
        
        score = 100  # Start with perfect score
        
        # Deduct points for cloud services
        cloud_services = len(found_keys)
        score -= (cloud_services * 15)
        
        # Deduct points for cloud configs
        cloud_configs = len([c for c in found_configs if "ollama" not in c.lower()])
        score -= (cloud_configs * 10)
        
        # Add points for local services
        if "Ollama (local models)" in found_configs:
            score += 10
        
        score = max(0, min(100, score))  # Clamp between 0-100
        
        if score >= 80:
            rating = "🟢 Low Risk"
            message = "Good privacy practices!"
        elif score >= 60:
            rating = "🟡 Medium Risk"
            message = "Some data exposure to cloud services"
        else:
            rating = "🔴 High Risk"
            message = "Significant data sharing with cloud services"
        
        print(f"  Score: {score}/100 - {rating}")
        print(f"  {message}")
        
        self.report["privacy_score"] = score
        return score
    
    def generate_recommendations(self):
        """Generate privacy improvement recommendations"""
        print("\n💡 Recommendations:")
        
        recommendations = [
            "Use Ollama for sensitive prompts",
            "Regularly delete cloud conversation history",
            "Opt out of training data usage where possible",
            "Use separate accounts for work vs personal",
            "Review API usage logs monthly",
            "Consider self-hosted alternatives"
        ]
        
        for i, rec in enumerate(recommendations, 1):
            print(f"  {i}. {rec}")
            self.report["recommendations"].append(rec)
    
    def save_report(self):
        """Save audit report to file"""
        filename = f"privacy_audit_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        with open(filename, 'w') as f:
            json.dump(self.report, f, indent=2)
        
        print(f"\n📄 Report saved to: {filename}")
        return filename
    
    def run_audit(self):
        """Run the complete privacy audit"""
        print("=" * 50)
        print("🔒 AI Privacy Audit Tool")
        print("=" * 50)
        
        # Run all checks
        found_keys = self.check_api_keys()
        found_configs = self.check_config_files()
        self.check_browser_storage()
        self.analyze_data_retention()
        score = self.calculate_privacy_score(found_keys, found_configs)
        self.generate_recommendations()
        
        # Save report
        report_file = self.save_report()
        
        print("\n" + "=" * 50)
        print("✅ Audit Complete!")
        print("=" * 50)
        
        return report_file


def main():
    """Run the privacy audit"""
    auditor = AIPrivacyAuditor()
    report_file = auditor.run_audit()
    
    print("\n🎯 Next Steps:")
    print("1. Review your audit report")
    print("2. Delete unnecessary cloud conversation history")
    print("3. Install Ollama for private AI usage")
    print("4. Consider which prompts need cloud vs local")


if __name__ == "__main__":
    main()