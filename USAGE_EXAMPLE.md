# MapleSeek Agentic Decompiler: Usage Example

This example demonstrates MapleSeek's agentic AI capabilities for intelligent Java decompilation.

## Quick Start

```bash
# Set up your DeepSeek API key
export DEEPSEEK_API_KEY=your_api_key_here

# Run the agentic decompiler on the sample
python main.py sample_input.mapleir workspace/output/ --verbose
```

## What Happens During Agentic Decompilation

### Phase 1: Codebase Analysis
```
Analyzing codebase relationships...
Found 3 classes to process
Phase 1: Analyzing class relationships...
```

The AI analyzes all classes to understand:
- `DoubleMathOperation$3` and `DoubleMathOperation$2` are inner classes
- `Calculations` is an independent utility class
- Relationships between mathematical operations

### Phase 2: Intelligent Processing Order
```
Processing order determined:
1. dev/sim0n/evaluator/util/stats/Calculations (base utility)
2. dev/sim0n/evaluator/operation/DoubleMathOperation$2 (inner class)
3. dev/sim0n/evaluator/operation/DoubleMathOperation$3 (inner class)
```

Classes are processed in dependency order for optimal results.

### Phase 3: Context-Aware Decompilation

For each class, the AI has access to:
- **Full MapleIR code** for the target class
- **Related class context** (parent classes, referenced types)
- **Previously decompiled classes** for consistency
- **Function calling** to request additional context

### Phase 4: Function Calling in Action

During decompilation, the AI may make function calls like:
```json
{
  "function_call": {
    "name": "get_class_context",
    "arguments": {
      "class_name": "dev/sim0n/evaluator/operation/DoubleMathOperation"
    }
  }
}
```

This allows the AI to understand the parent class structure when decompiling inner classes.

## Sample Output

### Calculations.java
```java
package dev.sim0n.evaluator.util.stats;

public class Calculations {
    
    public static double calculateMean(double[] values) {
        double sum = 0.0;
        for (double value : values) {
            sum += value;
        }
        return sum / values.length;
    }
    
    public static double calculateVariance(double[] values) {
        double mean = calculateMean(values);
        double variance = 0.0;
        for (double value : values) {
            variance += Math.pow(value - mean, 2);
        }
        return variance / values.length;
    }
    
    public static double calculateStandardDeviation(double[] values) {
        return Math.sqrt(calculateVariance(values));
    }
}
```

### DoubleMathOperation$2.java
```java
package dev.sim0n.evaluator.operation;

public class DoubleMathOperation$2 extends DoubleMathOperation {
    
    @Override
    public Double apply(Double left, Double right) {
        return left - right;
    }
    
    @Override
    public String getSymbol() {
        return "-";
    }
}
```

## Advanced Features Demonstrated

### 1. Context-Aware Type Resolution
The AI understands that `DoubleMathOperation$2` should extend `DoubleMathOperation` by analyzing the class hierarchy.

### 2. Consistent Naming
Variable names and method signatures are consistent across related classes.

### 3. Package Structure Preservation
The original package structure is preserved:
```
workspace/output/
├── dev/
│   └── sim0n/
│       └── evaluator/
│           ├── operation/
│           │   ├── DoubleMathOperation$2.java
│           │   └── DoubleMathOperation$3.java
│           └── util/
│               └── stats/
│                   └── Calculations.java
└── decompilation_summary.txt
```

### 4. Intelligent Method Reconstruction
The AI reconstructs method logic by understanding:
- SSA variable flow
- Control flow blocks
- Type inference from usage patterns

## Verbose Output Example

```bash
$ python main.py sample_input.mapleir workspace/output/ --verbose

MapleSeek v2.0.0 - Agentic Decompiler
Input file: sample_input.mapleir
Output directory: workspace/output/
AI Provider: deepseek
Initializing parser...
Initializing deepseek agentic AI client...
Setting up output directory...
Parsing MapleIR file...
Parsing classes...
Found 3 classes to process
Starting agentic decompilation process...
This includes codebase analysis and context-aware decompilation...
Phase 1: Analyzing class relationships...
Analyzing codebase relationships...
Decompiling class: dev/sim0n/evaluator/util/stats/Calculations
Successfully decompiled: dev/sim0n/evaluator/util/stats/Calculations
Decompiling class: dev/sim0n/evaluator/operation/DoubleMathOperation$2
Successfully decompiled: dev/sim0n/evaluator/operation/DoubleMathOperation$2
Decompiling class: dev/sim0n/evaluator/operation/DoubleMathOperation$3
Successfully decompiled: dev/sim0n/evaluator/operation/DoubleMathOperation$3
Phase 2: Writing decompiled classes to files...
Writing Java files ████████████████████████████████████████ 100%

Agentic decompilation complete!
Classes processed: 3
Files written: 3
Output directory: workspace/output/
Summary file: workspace/output/decompilation_summary.txt

Decompilation approach:
  - Analyzed class relationships and dependencies
  - Processed classes in optimal order
  - Used context-aware decompilation with function calling
  - AI could request additional context as needed

Written files:
  - workspace/output/dev/sim0n/evaluator/util/stats/Calculations.java
  - workspace/output/dev/sim0n/evaluator/operation/DoubleMathOperation$2.java
  - workspace/output/dev/sim0n/evaluator/operation/DoubleMathOperation$3.java
```

## Key Advantages of Agentic Approach

1. **Smarter Context Usage**: AI only requests context it needs, avoiding token waste
2. **Better Type Resolution**: Understanding of class hierarchies improves type inference
3. **Consistent Output**: Related classes have consistent naming and structure
4. **Error Recovery**: AI can request clarification when encountering ambiguous code
5. **Scalability**: Handles large codebases by processing classes incrementally

## Testing the Implementation

Run the test suite to verify everything works:

```bash
python test_agentic_decompiler.py
```

This tests:
- Parser functionality with the sample input
- AI client initialization
- Error handling for missing API keys

## Next Steps

- Try with your own MapleIR dumps
- Experiment with different AI providers (OpenAI vs DeepSeek)
- Use verbose mode to understand the agentic process
- Examine the generated `decompilation_summary.txt` for insights 