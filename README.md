# Take-Home Assignment - Guruprasath Gopal

This repository contains solutions to a take-home programming assignment with two distinct problems, implemented in Python.

## Project Structure

```
TakeHomeAssignment/
├── Assignment1/
│   └── main.py          # Word reversal implementation
├── Assignment2/
│   └── main.py          # Version update script
├── Makefile            # Build and run commands
├── requirements.txt     # Python dependencies (empty)
└── README.md         -> You are here !!!!
```

## Setup and Running

### Prerequisites

- Python 3.x
- Make (optional, for using Makefile commands)

### Quick Start

1. **Clone the repository and navigate to the project directory** `git clone https://github.com/Collaboration95/TakeHomeAssignment.git`

2. **Set up the environment and run all assignments:**

   ```bash
   make all
   ```

   This command will:

   - Clean up any previous runs
   - Create a Python virtual environment (if not exists)
   - Install dependencies
   - Run Assignment 1
   - Run Assignment 2 with test data

### Manual Setup

1. **Create virtual environment:**

   ```bash
   make ready
   ```

   Or manually:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install --upgrade pip
   ```

2. **Run individual assignments:**

   **Assignment 1 (Word Reversal):**

   ```bash
   make A1
   ```

   Or manually:

   ```bash
   cd Assignment1
   python main.py
   ```

   **Assignment 2 (Version Update):**

   ```bash
   make A2
   ```

   Or manually:

   ```bash
   cd Assignment2
   # Create test directory structure
   mkdir -p sample_source/develop/global/src
   echo "point=123," > sample_source/develop/global/src/SConstruct
   echo "ADLMSDK_VERSION_POINT= 123" > sample_source/develop/global/src/VERSION
   # Run with environment variables
   BuildNum="456" SourcePath="$(pwd)/sample_source" python main.py
   ```

### Cleanup

```bash
make cleanup
```

## Assignment Descriptions

### Assignment 1: Word Reversal

**Problem:** Reverse each word in a string while keeping punctuation and spaces unchanged. Words consist of letters and/or numbers.

**Example:**

- Input: `"String; 2be reversed..."`
- Output: `"gnirtS; eb2 desrever..."`

The solution uses an in-place modification approach with O(n) time complexity, where n is the string length.

### Assignment 2: Version Update Script

**Problem:** Update build version numbers in two files (`SConstruct` and `VERSION`) within a source directory structure. The version number comes from the `BuildNum` environment variable.

## Optimizations and Improvements

From the Original `Intern's code` , the following improvements were done to ensure production quality code

### Memory Optimizations

- **Assignment 1**: Improved `h_reverse_word` function to use O(m) space complexity where m is word length, instead of O(n) where n is string length
- **Assignment 2**: Added proper resource management using `with` statements for file operations

### Code Quality Improvements

- **Pure Functions**: Made `h_reverse_word` pure by creating copies instead of modifying in-place
- **DRY Principle**: Eliminated code duplication through refactoring
- **Structured Logging**: Added comprehensive logging with timestamps and log levels
- **Error Handling**: Added try-except blocks and proper validation

### Reliability Enhancements

- **Race Condition Fix**: Fixed issue where original files were deleted before temporary files were validated
- **UUID for File Safety**: Added unique identifiers to temporary files to prevent path conflicts
- **Input Validation**: Added validation for environment variables and file paths
- **Dependency Injection**: Refactored to call `create_config()` once and inject dependencies

### Performance Optimizations

- **Regex Fixes**: Corrected regex patterns for accurate version number updates
- **Single Validation Pass**: Optimized to validate source paths only once per execution

### Testing and Debugging

- **Comprehensive Test Suite**: Added extensive test cases for edge cases (empty strings, punctuation, multiple spaces, etc.)
- **Debug Information**: Added debug logging for configuration values during testing

## Technical Details

### Assignment 1 Algorithm

The word reversal uses a two-pointer approach:

1. Convert string to list for mutability
2. Iterate through characters, identifying alphanumeric sequences
3. Reverse each alphanumeric segment in-place
4. Join back to string

### Assignment 2 Implementation

- Uses dataclasses for configuration management
- Implements atomic file updates using temporary files
- Includes comprehensive error handling and logging
- Validates all inputs before processing
