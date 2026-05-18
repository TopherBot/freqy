# freqy

**freqy** – a minimal, zero‑dependency Python utility for counting word frequencies.

## Features
- Reads from a file or standard input.
- Supports Unicode and case‑insensitive counting.
- Outputs the *N* most frequent words (default 10).
- Perfect for quick text analysis in scripts or the terminal.

## Installation
```bash
# Clone the repository (or copy the single file)
git clone https://github.com/yourname/freqy.git
cd freqy
# No installation step needed – just run with Python 3.7+
```

## Usage
```bash
# From a file
python freqy.py -f path/to/text.txt -n 15

# From a pipe
cat mylog.log | python freqy.py -n 20
```

### Options
| Flag | Description |
|------|-------------|
| `-f`, `--file` | Path to a text file. If omitted, reads from `stdin`. |
| `-n`, `--top`  | Number of top words to display (default: 10). |
| `-i`, `--ignore-case` | Treat words case‑insensitively (default: on). |
| `-h`, `--help` | Show help message. |

## Example Output
```
1. the: 342
2. and: 287
3. to: 245
4. of: 232
5. a: 198
6. in: 176
7. is: 158
8. that: 152
9. it: 149
10. for: 143
```

## License
This project is released under the MIT License. See the `LICENSE` file for details.
