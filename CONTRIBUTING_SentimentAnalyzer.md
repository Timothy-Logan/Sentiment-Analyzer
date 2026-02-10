# Contributing to Sentiment Analyzer

Thank you for your interest in contributing to the Sentiment Analyzer! We welcome contributions from the community.

## Ways to Contribute

### 🐛 Report Bugs

Found a bug? Please open an issue with:
- Clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Your environment (OS, Python version)
- Text input that caused the issue
- Error messages or screenshots

### 💡 Suggest Features

Have an idea? Open an issue describing:
- The feature you'd like to see
- Why it would be useful
- Possible implementation approach
- Examples of similar features in other NLP tools

### 📝 Improve Documentation

Documentation improvements are always welcome:
- Fix typos or unclear explanations
- Add more example inputs/outputs
- Improve installation instructions
- Add tips for better results
- Document model limitations

### 🔧 Submit Code

1. **Fork** the repository
2. **Create a branch** for your feature
   ```bash
   git checkout -b feature/add-emotion-detection
   ```
3. **Make your changes**
   - Follow PEP 8 style guidelines
   - Add comments for complex logic
   - Update documentation if needed
   - Add docstrings to new functions
4. **Test your changes**
   - Test with various text inputs
   - Test edge cases (empty strings, very long text, special characters)
   - Verify model loads correctly
5. **Commit with clear message**
   ```bash
   git commit -m "Add: support for multi-language sentiment analysis"
   ```
6. **Push to your fork**
   ```bash
   git push origin feature/add-emotion-detection
   ```
7. **Open a Pull Request**
   - Describe your changes clearly
   - Reference any related issues
   - Include example outputs if applicable

## Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/sentiment-analyzer
cd sentiment-analyzer

# Install dependencies
pip install -r requirements.txt

# Run the analyzer
python sentiment_analyzer.py

# Run tests (if available)
python -m unittest discover tests
```

## Code Style Guidelines

- Follow [PEP 8](https://pep8.org/) Python style guide
- Use descriptive variable names (e.g., `sentiment_score` not `ss`)
- Add docstrings to all functions and classes
- Keep functions focused and under 50 lines when possible
- Comment NLP-specific logic and model operations
- Use type hints for function parameters and returns

Example:
```python
def analyze_batch(self, texts: List[str]) -> List[Dict[str, any]]:
    """
    Analyze sentiment of multiple texts efficiently.
    
    Args:
        texts: List of text strings to analyze
        
    Returns:
        List of dictionaries containing sentiment results
        
    Example:
        >>> analyzer = SentimentAnalyzer()
        >>> results = analyzer.analyze_batch(["Great!", "Terrible"])
        >>> print(results[0]['sentiment'])
        'POSITIVE'
    """
    # Implementation here
```

## Testing

Before submitting a pull request:

1. **Test with various inputs**:
   ```bash
   python sentiment_analyzer.py
   # Try these test cases:
   # Positive: "I love this!", "Best day ever!"
   # Negative: "This is awful", "Worst experience"
   # Neutral: "The meeting is at 3pm"
   # Edge cases: "", "!!!!", very long text
   # Special characters: "😊 Happy", "C'est magnifique"
   ```

2. **Run unit tests**:
   ```bash
   python -m unittest discover tests
   ```

3. **Check code style**:
   ```bash
   # Install flake8 if needed
   pip install flake8
   
   # Run linter
   flake8 sentiment_analyzer.py --max-line-length=100
   ```

4. **Test model loading**:
   ```bash
   # Ensure model downloads correctly on first run
   python sentiment_analyzer.py
   ```

## Project Structure

```
sentiment-analyzer/
├── sentiment_analyzer.py  # Main CLI application
├── requirements.txt       # Python dependencies
├── tests/                # Unit tests
│   ├── __init__.py
│   └── test_sentiment_analyzer.py
├── LICENSE               # MIT License
├── README.md            # Project documentation
├── CONTRIBUTING.md      # This file
└── .gitignore          # Git ignore rules
```

## Adding New Features

### Want to add emotion detection?

1. Research available emotion detection models on Hugging Face
2. Add new model loading in `__init__` method
3. Create new method for emotion analysis
4. Document in README and docstrings

### Want to support multiple languages?

1. Find multilingual sentiment models on Hugging Face
2. Add language detection or parameter
3. Update model initialization to support languages
4. Test with non-English text
5. Document supported languages

### Want to add batch file processing?

1. Add method to read files (CSV, TXT, JSON)
2. Process multiple texts efficiently
3. Add export functionality for results
4. Update CLI to accept file paths

## Feature Ideas

Looking for something to work on? Here are some ideas:

**Easy:**
- Add progress bar for batch processing
- Add support for reading from stdin
- Improve error messages
- Add command-line arguments for options

**Medium:**
- Add emotion detection (happy, sad, angry, etc.)
- Support multiple languages
- Add batch file processing (CSV, JSON)
- Cache model to disk for faster loading
- Add confidence threshold filtering

**Advanced:**
- Create REST API endpoint with FastAPI
- Add fine-tuning capability for custom domains
- Implement aspect-based sentiment analysis
- Add visualization of sentiment trends
- Create web interface

## Model Guidelines

When working with transformer models:
- Use models from Hugging Face's model hub
- Document model source and version
- Include model performance metrics
- Consider model size and loading time
- Test with various input lengths
- Handle model errors gracefully

### Recommended Models

For sentiment analysis:
- `distilbert-base-uncased-finetuned-sst-2-english` (current)
- `cardiffnlp/twitter-roberta-base-sentiment`
- `nlptown/bert-base-multilingual-uncased-sentiment`

For emotions:
- `j-hartmann/emotion-english-distilroberta-base`
- `bhadresh-savani/distilbert-base-uncased-emotion`

## Pull Request Process

1. Update the README.md with details of changes if applicable
2. Update requirements.txt if you add new dependencies
3. Add or update tests for new features
4. Update docstrings and comments
5. Your PR will be reviewed within 2-3 days
6. Address any feedback from reviewers
7. Once approved, your changes will be merged!

## Performance Considerations

When adding features:
- Consider model loading time
- Minimize memory usage where possible
- Batch processing for efficiency
- Cache results when appropriate
- Document performance characteristics

## Questions or Need Help?

Feel free to:
- Open an issue for discussion
- Email: [tjlogan9@gmail.com](mailto:tjlogan9@gmail.com)
- Check existing issues for similar questions
- Ask about NLP concepts or transformer models
- Request help with Hugging Face API

## Code of Conduct

### Our Standards

- Be respectful and constructive
- Welcome newcomers and help them learn
- Focus on what is best for the project
- Show empathy towards other contributors
- Give and accept constructive feedback gracefully

### Unacceptable Behavior

- Harassment or discriminatory language
- Trolling or insulting comments
- Publishing others' private information
- Other conduct which could reasonably be considered inappropriate

## Recognition

Contributors will be:
- Listed in the project's acknowledgments
- Credited in release notes for their contributions
- Invited to collaborate on future enhancements
- Mentioned in README if making significant contributions

## Resources

Helpful links for contributors:
- [Hugging Face Transformers Docs](https://huggingface.co/docs/transformers/index)
- [Sentiment Analysis Guide](https://huggingface.co/tasks/sentiment-analysis)
- [Python NLP Tutorial](https://realpython.com/natural-language-processing-spacy-python/)
- [DistilBERT Paper](https://arxiv.org/abs/1910.01108)

## License

By contributing, you agree that your contributions will be licensed under the project's MIT License.

---

Thank you for helping improve the Sentiment Analyzer! 🎭
