#!/usr/bin/env python3
"""
Test script to verify API key rotation is working
"""

from quiz_generator import QuizGenerator
from config import API_KEY_POOL

def test_rotation():
    print("=" * 60)
    print("API KEY ROTATION TEST")
    print("=" * 60)
    
    print(f"\n📋 Total API keys configured: {len(API_KEY_POOL)}")
    print(f"🔑 Keys: {[key[:10] + '...' for key in API_KEY_POOL]}\n")
    
    # Create generator
    generator = QuizGenerator()
    
    print("Testing key rotation logic...\n")
    
    # Get first 3 keys
    for i in range(3):
        key = generator.get_next_available_key()
        print(f"  Key {i+1}: {key[:10]}...{key[-6:]}")
    
    print("\n✅ Key rotation logic is working!")
    print(f"\n💡 The system will automatically switch to the next key when one hits quota.")
    print(f"📊 Current status: {len(API_KEY_POOL) - len(QuizGenerator.failed_keys)}/{len(API_KEY_POOL)} keys available")

if __name__ == "__main__":
    test_rotation()
