# MapleSeek: Agentic AI-Powered Java Decompiler

MapleSeek is an advanced AI-powered decompiler that converts MapleIR SSA IR dumps back to readable Java source code using agentic artificial intelligence techniques.

## 🚀 Key Features

- **Agentic AI Decompilation**: Uses function calling and iterative reasoning for intelligent code reconstruction
- **Context-Aware Processing**: Analyzes class relationships and dependencies before decompilation
- **Real-Time AI Streaming**: Watch AI responses stream in real-time with a beautiful CLI interface
- **Enhanced UI**: Rich terminal interface with progress bars, panels, and syntax highlighting
- **Dependency Resolution**: Processes classes in optimal order based on inheritance and reference relationships
- **Intelligent Context Retrieval**: AI can request additional class context as needed during decompilation
- **Support for Complex Hierarchies**: Handles inner classes, inheritance, and interface implementations
- **Multiple AI Providers**: Supports DeepSeek (default) and OpenAI

## 🏗️ Architecture

MapleSeek uses a sophisticated agentic approach:

1. **Codebase Analysis**: First analyzes all classes to understand relationships
2. **Dependency Mapping**: Creates a dependency graph for optimal processing order
3. **Context-Aware Decompilation**: Provides relevant class context for each decompilation
4. **Function Calling**: AI can request additional context during the decompilation process
5. **Iterative Refinement**: Supports multiple rounds of context gathering and refinement

## 📦 Installation

```bash
# Clone the repository
git clone <repository-url>
cd maple-deepseek

# Install dependencies
pip install -r requirements.txt

# Or using uv (recommended)
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
python main.py input.mapleir output_directory/

# Using OpenAI
python main.py input.mapleir output_directory/ --provider openai

# Verbose output with real-time AI streaming display
python main.py input.mapleir output_directory/ --verbose
```

### Advanced Usage
```bash
# With specific API key
python main.py input.mapleir output_directory/ --api-key your_key_here

# Disable streaming for traditional output
python main.py input.mapleir output_directory/ --no-stream

# Full verbose output with streaming and enhanced UI
python main.py input.mapleir output_directory/ --verbose --stream
```

### Enhanced CLI Features
The new enhanced CLI provides:
- 🎨 **Beautiful welcome banner** with ASCII art
- 📊 **Real-time progress bars** for all operations
- 🖥️ **Streaming AI response window** showing live decompilation process
- 🎯 **Phase-based display** clearly showing analysis and decompilation stages
- 📈 **Detailed statistics** with processing time and success rates
- 🌈 **Syntax highlighting** for AI responses and code snippets

### Demo the Enhanced UI
```bash
# Try the demo to see all UI features
python demo_enhanced_cli.py streaming    # See real-time streaming
python demo_enhanced_cli.py progress     # See progress bars
python demo_enhanced_cli.py components   # See all UI components

# Test the UI fixes
python test_enhanced_ui_fix.py streaming # Test streaming without conflicts
python test_enhanced_ui_fix.py progress  # Test progress bars separately
```

## 🧠 How It Works

### Phase 1: Codebase Analysis
The AI analyzes all MapleIR classes to understand:
- Inheritance hierarchies
- Interface implementations
- Cross-class references
- Inner class relationships

### Phase 2: Dependency Ordering
Classes are sorted into optimal processing order:
- Base classes before derived classes
- Referenced classes before classes that use them
- Independent classes can be processed in parallel

### Phase 3: Context-Aware Decompilation
For each class, the AI has access to:
- Full MapleIR code for the target class
- Context of related classes (superclasses, interfaces)
- Previously decompiled classes for consistency
- Function calling capabilities to request additional context

### Phase 4: Iterative Refinement
The AI can:
- Request additional class definitions
- Access previously decompiled code
- Make multiple passes for complex relationships

## 📁 Output Structure

```
output_directory/
├── com/
│   └── example/
│       ├── BaseClass.java
│       ├── DerivedClass.java
│       └── InnerClass$SubClass.java
├── org/
│   └── another/
│       └── Package.java
└── decompilation_summary.txt
```

## 🔍 Example

```bash
# Example with the provided sample
python main.py sample_input.mapleir workspace/output/ --verbose
```

This will:
1. Analyze the sample MapleIR classes
2. Identify relationships between `DoubleMathOperation` inner classes and `Calculations`
3. Process them in dependency order
4. Generate clean Java code with proper package structure

## 🛠️ Development

### Testing
```bash
python test_agentic_decompiler.py
```

### Project Structure
```
mapleseek/
├── ai_client.py       # Agentic AI client with function calling
├── parser.py          # MapleIR format parser
├── output.py          # Java file writer
└── cli.py            # Command-line interface
```

## 🎭 Agentic Features

### Function Calling
The AI can use these functions during decompilation:
- `get_class_context(class_name)`: Get MapleIR for any class in the codebase
- `get_decompiled_class(class_name)`: Get already decompiled Java code

### Context Awareness
- Full codebase visibility for relationship analysis
- Smart context provision based on dependencies
- Consistent naming and structure across related classes

### Intelligent Processing
- Automatic dependency resolution
- Optimal processing order
- Context-driven decision making

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests: `python test_agentic_decompiler.py`
5. Submit a pull request

## 📄 License

[License information here]

## 🙏 Acknowledgments

- MapleIR project for the IR format
- DeepSeek for providing powerful AI capabilities
- OpenAI for their API standards
