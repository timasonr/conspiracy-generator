#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import json
import os
from dotenv import load_dotenv
import openai

# Load environment variables from .env file
load_dotenv()

# OpenAI API setup - set key directly
openai.api_key = "enter your key here"

def load_templates():
    """Load conspiracy theory templates from JSON file."""
    with open("templates.json", "r", encoding="utf-8") as file:
        return json.load(file)

def generate_conspiracy_theory(templates, theme=None):
    """Generate an absurd conspiracy theory based on templates."""
    if theme and theme in templates:
        selected_templates = templates[theme]
    else:
        # If no theme is specified or it doesn't exist, choose a random theme
        theme = random.choice(list(templates.keys()))
        selected_templates = templates[theme]
    
    # Select random elements for the conspiracy theory
    who = random.choice(selected_templates["who"])
    action = random.choice(selected_templates["action"])
    target = random.choice(selected_templates["target"])
    how = random.choice(selected_templates["how"])
    
    # Form the conspiracy theory
    theory = f"{who} {action} {target} {how}"
    
    return theory, theme

def enhance_with_gpt(theory):
    """Enhance the conspiracy theory using GPT."""
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an absurd conspiracy theory generator. Create a more detailed and humorous version of the conspiracy theory by adding details and pseudo-scientific explanations. Keep it absurd and use no more than 3-4 sentences."},
                {"role": "user", "content": f"Enhance this conspiracy theory: {theory}"}
            ],
            max_tokens=250
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error when calling OpenAI API: {e}")
        return theory

def debunk_conspiracy(theory):
    """Debunk the absurdity of the conspiracy with GPT."""
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a skeptic and rationalist. Your task is to debunk an absurd conspiracy theory in a humorous and educational way. Point out logical fallacies, scientific facts, and common sense showing why the theory cannot be true. Keep a humorous tone and use no more than 3-4 sentences."},
                {"role": "user", "content": f"Debunk this absurd conspiracy theory: {theory}"}
            ],
            max_tokens=250
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error when calling OpenAI API: {e}")
        return "Failed to get theory debunking due to API error."

def create_theory_with_gpt(theme_description):
    """Create a completely new conspiracy theory using GPT."""
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an absurd conspiracy theory generator. Create an absurd but creative conspiracy theory on the given topic. Make it humorous, somewhat sci-fi, and completely ridiculous. Use 2-3 sentences."},
                {"role": "user", "content": f"Create an absurd conspiracy theory on the topic of '{theme_description}'"}
            ],
            max_tokens=250
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error when calling OpenAI API: {e}")
        return "Failed to generate theory due to API error."

def show_menu():
    print("\n" + "="*50)
    print("ABSURD CONSPIRACY THEORY GENERATOR")
    print("="*50)
    print("1. Generate a random theory (basic template + ChatGPT)")
    print("2. Choose a theme for generation (basic template + ChatGPT)")
    print("3. Create a completely new theory with ChatGPT")
    print("4. Debunk current theory")
    print("5. Exit")
    print("="*50)
    choice = input("Choose an action (1-5): ")
    return choice

def main():
    try:
        templates = load_templates()
        current_theory = None
        current_theme = None
        
        print("\nWelcome to the Absurd Conspiracy Theory Generator!")
        print("All theories are generated and enhanced using ChatGPT.")
        
        while True:
            choice = show_menu()
            
            if choice == "1":
                # Generate a basic theory and immediately enhance it with ChatGPT
                base_theory, theme = generate_conspiracy_theory(templates)
                print(f"\nGenerating a theory on the theme: {theme}...")
                current_theme = theme
                
                print("\nContacting ChatGPT to create a conspiracy theory...")
                current_theory = enhance_with_gpt(base_theory)
                
                print(f"\n[Theme: {theme}]")
                print(current_theory)
                
            elif choice == "2":
                print("\nAvailable themes:")
                for i, theme in enumerate(templates.keys(), 1):
                    print(f"{i}. {theme}")
                print(f"{len(templates.keys()) + 1}. Random theme")
                
                try:
                    theme_choice = int(input(f"Select a theme (1-{len(templates.keys()) + 1}): "))
                    if 1 <= theme_choice <= len(templates.keys()):
                        selected_theme = list(templates.keys())[theme_choice - 1]
                        base_theory, theme = generate_conspiracy_theory(templates, selected_theme)
                        current_theme = theme
                        
                        print("\nContacting ChatGPT to create a conspiracy theory...")
                        current_theory = enhance_with_gpt(base_theory)
                        
                        print(f"\n[Theme: {theme}]")
                        print(current_theory)
                        
                    elif theme_choice == len(templates.keys()) + 1:
                        base_theory, theme = generate_conspiracy_theory(templates)
                        current_theme = theme
                        
                        print("\nContacting ChatGPT to create a conspiracy theory...")
                        current_theory = enhance_with_gpt(base_theory)
                        
                        print(f"\n[Theme: {theme}]")
                        print(current_theory)
                    else:
                        print("Invalid theme selection.")
                except ValueError:
                    print("Please enter a number.")
                    
            elif choice == "3":
                custom_themes = ["Food and Cuisine", "Sports", "Space", "Medicine", 
                                "Education", "Animals", "Transportation", "Fashion", 
                                "Art", "History", "Custom option"]
                
                print("\nChoose a theme for generating a new theory:")
                for i, theme in enumerate(custom_themes, 1):
                    print(f"{i}. {theme}")
                
                try:
                    theme_choice = int(input(f"Select a theme (1-{len(custom_themes)}): "))
                    if 1 <= theme_choice < len(custom_themes):
                        theme_description = custom_themes[theme_choice - 1]
                        current_theme = theme_description
                    elif theme_choice == len(custom_themes):
                        theme_description = input("Enter your theme: ")
                        current_theme = theme_description
                    else:
                        print("Invalid choice. Using a random theme.")
                        theme_description = random.choice(custom_themes[:-1])
                        current_theme = theme_description
                        
                    print(f"\nCreating a conspiracy theory on the theme '{theme_description}'...")
                    current_theory = create_theory_with_gpt(theme_description)
                    
                    print(f"\n[Theme: {current_theme}]")
                    print(current_theory)
                    
                except ValueError:
                    print("Please enter a number. Using a random theme.")
                    theme_description = random.choice(custom_themes[:-1])
                    current_theme = theme_description
                    
                    print(f"\nCreating a conspiracy theory on the theme '{theme_description}'...")
                    current_theory = create_theory_with_gpt(theme_description)
                    
                    print(f"\n[Theme: {current_theme}]")
                    print(current_theory)
                    
            elif choice == "4":
                if current_theory is None:
                    print("\nFirst generate a theory (options 1, 2, or 3).")
                else:
                    print("\nContacting ChatGPT to debunk the theory...")
                    debunked = debunk_conspiracy(current_theory)
                    
                    print(f"\n[Theme: {current_theme}]")
                    print("\nConspiracy theory:")
                    print(current_theory)
                    print("\nDebunking:")
                    print(debunked)
                    
            elif choice == "5":
                print("\nUntil the next conspiracy! 👽")
                break
                
            else:
                print("\nInvalid choice. Please choose from 1 to 5.")
                
    except FileNotFoundError:
        print("Error: Template file not found. Make sure the templates.json file exists.")
    except json.JSONDecodeError:
        print("Error: Unable to read the template file. Check the JSON file format.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main() 