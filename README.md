<img src=".docs/logo.png" width="100px"/>

# MapleSeek

MapleSeek is an experimental AI-slop powered decompiler that converts MapleIR SSA IR dumps back to readable Java source code using agentic ai slop. Slop for the purpose of slop, made by slop.

## 📦 Installation

```bash
uv sync
```

## 🔧 Setup

### DeepSeek (Default)
```bash
export DEEPSEEK_API_KEY=your_deepseek_api_key_here
```

### OpenAI (Alternative)
```bash
export OPENAI_API_KEY=your_openai_api_key_here
```

## 🎯 Usage

### Basic Usage
```bash
# Using DeepSeek (default) with enhanced UI and streaming
uv run mapleseek input.mapleir output_directory/

# Using OpenAI
uv run mapleseek input.mapleir output_directory/ --provider openai

# Verbose output with real-time AI streaming display
uv run mapleseek input.mapleir output_directory/ --verbose
```

### Advanced Usage
```bash
# With specific API key
uv run mapleseek input.mapleir output_directory/ --api-key your_key_here

# Disable streaming for traditional output
uv run mapleseek input.mapleir output_directory/ --no-stream

# Full verbose output with streaming and enhanced UI
uv run mapleseek input.mapleir output_directory/ --verbose --stream
```


