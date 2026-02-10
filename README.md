# Sentiment Analyzer 🎭

![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![Transformers](https://img.shields.io/badge/transformers-4.30-orange.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

A command-line sentiment analysis tool powered by state-of-the-art transformer models. Quickly determine if text expresses positive or negative sentiment with confidence scores.

## Features

- 🎯 **Accurate Analysis** - Uses DistilBERT model fine-tuned on sentiment tasks
- 💯 **Confidence Scores** - Know how certain the model is
- ⚡ **Fast Inference** - Optimized for quick responses
- 🎨 **Color-Coded Output** - Easy-to-read results
- 📝 **Simple CLI** - User-friendly interface

## Technologies

- **Python 3.9+**
- **Transformers** - Hugging Face transformers library
- **PyTorch** - Deep learning framework
- **DistilBERT** - Lightweight BERT model (66M parameters)

## Installation

### Prerequisites
- Python 3.9 or higher
- pip package manager
- 2GB free disk space (for model download)

### Setup

```bash
# Clone the repository
git clone https://github.com/Timothy-Logan/sentiment-analyzer
cd sentiment-analyzer

# Install dependencies
pip install -r requirements.txt

# Run the analyzer
python sentiment_analyzer.py
```

## Usage

### Interactive Mode

```bash
python sentiment_analyzer.py
```

Then enter text when prompted:

```
==================================================
     SENTIMENT ANALYZER
     Powered by Transformers
==================================================

Enter text to analyze (or 'quit' to exit)
Examples:
  - 'This is amazing!'
  - 'I'm really disappointed'

📝 Text: I absolutely love this product!

Text: I absolutely love this product!
Sentiment: POSITIVE 😊
Confidence: 99.9%
--------------------------------------------------
```

## Examples

### Positive Sentiment
```
Input: "This is the best day ever!"
Output: POSITIVE 😊 (99.8% confidence)
```

### Negative Sentiment
```
Input: "I hate when things go wrong"
Output: NEGATIVE 😟 (99.2% confidence)
```

### Mixed/Neutral
```
Input: "The meeting is at 3pm"
Output: NEUTRAL (classifier returns best match)
```

## Use Cases

Perfect for:
- **Social Media Monitoring** - Track brand sentiment
- **Customer Feedback** - Analyze product reviews
- **Content Moderation** - Flag negative comments
- **Market Research** - Gauge public opinion
- **Email Triage** - Prioritize urgent/negative emails

## How It Works

This tool uses a **DistilBERT** model fine-tuned on the **SST-2** (Stanford Sentiment Treebank) dataset. The model:

1. Tokenizes input text into sub-word units
2. Processes through 6-layer transformer
3. Classifies as POSITIVE or NEGATIVE
4. Returns confidence score

**Performance:**
- Accuracy: ~92% on SST-2 benchmark
- Speed: ~0.1 seconds per sentence
- Model size: 268 MB

## Technical Details

### Model Architecture
- **Base**: DistilBERT (distilled version of BERT)
- **Parameters**: 66 million
- **Training Data**: SST-2 dataset (67k movie reviews)
- **Fine-tuning**: Sentiment classification task

### System Requirements

**Minimum:**
- Python 3.9+
- 2GB RAM
- 500MB disk space

**Recommended:**
- Python 3.10+
- 4GB RAM
- SSD storage

## Limitations

- Works best with English text
- Trained on movie reviews (may not generalize to all domains)
- Cannot detect sarcasm or complex emotions
- Binary classification (pos/neg), no neutral class
- Struggles with very short text (<3 words)

## Future Improvements

- [ ] Multi-language support
- [ ] Fine-grained emotions (happy, sad, angry, etc.)
- [ ] Batch file processing
- [ ] Export results to CSV/JSON
- [ ] Web API endpoint
- [ ] Confidence threshold adjustment

## Contributing

Contributions welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Hugging Face](https://huggingface.co/) for the transformers library
- [Stanford](https://nlp.stanford.edu/sentiment/) for the SST-2 dataset
- [DistilBERT paper](https://arxiv.org/abs/1910.01108) by Sanh et al.

## Contact

**Timothy Logan**  
📧 Email: [tjlogan9@gmail.com](mailto:tjlogan9@gmail.com)  
💼 LinkedIn: [linkedin.com/in/timothyjlogan](https://linkedin.com/in/timothyjlogan)  
🐙 GitHub: [@Timothy-Logan](https://github.com/Timothy-Logan)

---

*Built with ❤️ using Transformers*
