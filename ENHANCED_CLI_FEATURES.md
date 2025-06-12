# Enhanced CLI Features for MapleSeek

MapleSeek now includes a completely redesigned command-line interface with real-time AI streaming and beautiful visual components.

## 🎨 Visual Enhancements

### Welcome Banner
```
   __  __             _      ____            _    
  |  \/  | __ _ _ __ | | ___/ ___|  ___  ___| | __
  | |\/| |/ _` | '_ \| |/ _ \___ \ / _ \/ _ \ |/ /
  | |  | | (_| | |_) | |  __/___) |  __/  __/   < 
  |_|  |_|\__,_| .__/|_|\___|____/ \___|\___|_|\_\
               |_|                                 
```

- Displays an attractive ASCII art banner on startup
- Shows version information and subtitle
- Sets the professional tone for the application

### Configuration Display
- Beautiful tabular display of current settings
- Shows input file, output directory, AI provider, and options
- Color-coded for easy reading

### Phase-Based Processing Display
- **Phase 1**: Codebase Analysis with clear indicators
- **Phase 2**: Agentic Decompilation with progress tracking
- Visual separation between different processing stages

## 🖥️ Real-Time AI Streaming Window

### Streaming Display Features
- **Live AI Response**: Watch AI responses appear in real-time as they're generated
- **Syntax Highlighting**: JSON responses are syntax-highlighted for readability
- **Progress Indicators**: Shows character count and streaming status
- **Per-Class Streaming**: Each class gets its own streaming session

### Streaming Window Layout
```
┌─ 🤖 AI Decompiling: com.example.MyClass ─────── Press Ctrl+C to cancel ─┐
│                                                                          │
│ {                                                                        │
│   "class_name": "com.example.MyClass",                                  │
│   "package": "com.example",                                             │
│   "imports": ["java.util.List"],                                        │
│   "java_code": "package com.example;\n\nimport java.util.List;\n\n..."  │
│ }                                                                        │
│                                                                          │
└─ 📝 Accumulated: 1,247 chars ─────────────────────────────────────────┘
```

### Streaming Controls
- **Start/Stop**: Automatic management of streaming sessions
- **Threading**: Runs in separate thread for responsive UI
- **Error Handling**: Graceful handling of streaming errors
- **Memory Management**: Efficient handling of large responses

## 📊 Enhanced Progress Tracking

### Progress Bars
- **Rich Progress Bars**: Beautiful progress indicators with multiple columns
- **Time Tracking**: Shows elapsed time and estimated completion
- **Percentage Display**: Real-time percentage completion
- **Task Descriptions**: Clear labels for what's being processed

### Progress Bar Example
```
Decompiling classes ████████████████████ 100%  •  (3/3)  •  0:00:45
```

### Multiple Progress Types
- **Class Analysis**: Progress during codebase analysis phase
- **Decompilation**: Progress during AI decompilation phase
- **File Writing**: Progress during output file generation

## 🎯 Status and Result Display

### Class Processing Results
- ✅ **Success Indicators**: Green checkmarks for successful decompilations
- ❌ **Error Indicators**: Red X marks with detailed error messages
- 📝 **Info Messages**: Blue info icons for general status updates

### Result Summary Table
```
┌─ 📊 Decompilation Statistics ─┐
│ Total Classes      │ 15       │
│ ✅ Successful      │ 14       │
│ ❌ Failed          │ 1        │
│ ⏱️ Processing Time │ 45.2s    │
│ 📁 Output Dir      │ ./output │
│ 📄 Summary File    │ sum.md   │
└────────────────────┴──────────┘
```

## 🛠️ New Command-Line Options

### Streaming Control
```bash
# Enable streaming (default)
mapleseek input.mapleir output/ --stream

# Disable streaming for traditional output
mapleseek input.mapleir output/ --no-stream
```

### Verbose Mode Enhancements
```bash
# Enhanced verbose mode with streaming display
mapleseek input.mapleir output/ --verbose
```

### Provider Selection
```bash
# DeepSeek with enhanced UI (default)
mapleseek input.mapleir output/ --provider deepseek

# OpenAI with enhanced UI
mapleseek input.mapleir output/ --provider openai
```

## 🚀 Technical Implementation

### UI Architecture
- **Rich Library**: Uses `rich` for terminal formatting and layout
- **Threading**: Streaming display runs in separate thread
- **Queue-Based Communication**: Thread-safe message passing
- **Layout Management**: Dynamic layout updates for streaming content

### Components
- **EnhancedUI Class**: Main UI manager with all display methods
- **StreamingDisplay Class**: Real-time streaming window manager
- **Progress Management**: Custom progress bar configurations
- **Error Handling**: Graceful error display and recovery

### Performance Features
- **Non-Blocking UI**: Streaming doesn't block main processing
- **Efficient Updates**: Optimized refresh rates (10 FPS)
- **Memory Efficient**: Proper cleanup of streaming resources
- **Responsive Design**: Adapts to different terminal sizes

## 🧪 Demo and Testing

### Interactive Demos
```bash
# Demo streaming functionality
python demo_enhanced_cli.py streaming

# Demo progress bars
python demo_enhanced_cli.py progress

# Demo all UI components
python demo_enhanced_cli.py components
```

### Testing Features
- **Simulated Streaming**: Realistic AI response simulation
- **Progress Simulation**: Multi-step progress demonstration
- **Error Scenarios**: Error handling demonstration
- **Component Showcase**: All UI components in action

## 📋 Backwards Compatibility

### Legacy Support
- **Non-Streaming Mode**: Traditional output still available with `--no-stream`
- **Fallback Display**: Graceful degradation if rich components fail
- **API Compatibility**: All existing command-line arguments still work
- **Error Recovery**: Fallback to simple text output on UI errors

### Migration Path
- **Seamless Upgrade**: No changes needed to existing scripts
- **Optional Features**: Enhanced features are additive, not replacement
- **Configuration**: Same environment variables and setup process

## 🎯 User Experience Improvements

### Visual Feedback
- **Clear Progress**: Always know what's happening and how long it will take
- **Real-Time Updates**: See AI working in real-time
- **Error Context**: Clear error messages with context
- **Success Celebration**: Clear indication of successful completion

### Professional Appearance
- **Consistent Styling**: Professional color scheme throughout
- **Structured Layout**: Organized information presentation
- **Modern Terminal UI**: Takes advantage of modern terminal capabilities
- **Accessibility**: Clear contrast and readable fonts

This enhanced CLI transforms MapleSeek from a simple command-line tool into a modern, professional application with real-time feedback and beautiful visual presentation. 