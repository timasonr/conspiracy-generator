# Absurd Conspiracy Theory Generator

A Python program that generates funny and absurd conspiracy theories using ChatGPT. The program creates conspiracy theories, enhances them, and provides humorous debunkings using the OpenAI API.

## Installation

1. Clone the repository:
```
git clone https://github.com/timasonr/conspiracy-generator.git
cd conspiracy-generator
```

2. Install dependencies:
```
pip install python-dotenv openai
```

3. Create a `.env` file in the root directory and add your OpenAI API key:
```
OPENAI_API_KEY=your_openai_api_key_here
```

## Usage

### Interactive Mode:

For a convenient interaction with the program, use the interactive mode:
```
python interactive.py
```

In this mode, you'll get a menu with options to:
- Generate theories based on templates and ChatGPT
- Choose a specific theme for generation
- Create completely new theories using ChatGPT
- Debunk theories using ChatGPT

### Command Line Mode:

```
python main.py
```

This command will generate one random conspiracy theory on a random theme using ChatGPT.

### Additional Command Line Options:

- `-t`, `--theme` - Choose a specific theme ("politics", "showbiz", "tech", "free"):
```
python main.py --theme politics
```

- `-c`, `--custom` - Set your own theme for conspiracy theory generation:
```
python main.py --custom "Internet of Things"
```

- `-d`, `--debunk` - Include debunking of the theory using ChatGPT:
```
python main.py --debunk
```

- `-n`, `--count` - Number of theories to generate:
```
python main.py --count 3
```

You can combine these options:
```
python main.py --theme tech --debunk --count 2
```

For complete generation freedom:
```
python main.py --custom "Music" --debunk
```

## Output Examples

### Template-based theory + ChatGPT:
```
[Theme: tech]
Don't believe the official story! Corporate IT departments control the internet through search engines using quantum computers. Each search query activates hidden algorithms that analyze your psychological patterns and preferences. IT specialists from major corporations reprogram quantum systems at night to intercept your brain waves through monitor radiation. Your data is already stored in a secret repository at the bottom of the Pacific Ocean!
```

### With debunking:
```
[Theme: tech]
Corporate IT departments control the internet through search engines using quantum computers

Debunking:
Let's be honest: if corporate IT departments could actually control the internet, they would first fix the printers in their own offices! Quantum computers today have very limited applications and require conditions close to absolute zero (-273°C), making their mass use impossible. Plus, creating a global control system would require incredible international cooperation between competing companies, and we know they can't even agree on charging port standards!
```

## Template Customization

Templates for basic generation are stored in the `templates.json` file. You can edit existing themes or add new ones by following the format in this file. They are used as a basis for further enhancement of theories using ChatGPT.

## License

MIT 
