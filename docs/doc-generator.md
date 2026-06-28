### 📄 `doc_generator.README.md`

```markdown
# Documentation Generator (`doc_generator.py`)

A data transformation pipeline that consumes raw tabular export inventories and reorganizes them into human-navigable, markdown-based reference libraries.

## Technical Design & Strategy

### Environment Tree Mirroring
Rather than generating a flat file dump that strips away operational context, the engine reads the absolute paths recorded in the source data and strips structural roots (such as drive letters or mounting prefixes). It uses these relative paths to dynamically replicate the host operating system's native directory structure inside your target documentation folder.

### Index Generation & Scoping
To provide seamless navigation without causing immense file sizes or slow rendering times, the tool builds a nested index tree:
* **Root Index:** A master `README.md` gateway listing every directory analyzed and linking directly down into the structure.
* **Contextual Directory READMEs:** A separate `README.md` placed in *every individual subfolder*, acting as a local catalog mapping only the specific binaries housed in that precise directory.

### Name Collision Handling
Windows systems frequently maintain identical binary names across different directories to preserve application compatibility (e.g., separate variations of `ntdll.dll` or `kernel32.dll` in `System32` vs `SysWOW64`). To prevent target documentation profiles from clobbering or overwriting one another, the script suffixes individual file titles with the first eight characters of the binary's unique SHA256 cryptographic fingerprint:

```text
Format:  [binary_name]_[short_sha256].md
Example: ntdll_a1b2c3d4.md
```

### 📄 `doc_generator.py` Argument Specification

```markdown
## Argument Specification

```cmd
python doc_generator.py <input_csv_path> <output_markdown_directory>
```
* `input_csv_path`: The file path pointing to the completed dataset from the collector tool (e.g., `C:\dev\inventory.csv`).
* `output_markdown_directory`: The folder location where the mirrored markdown documentation structure will be created (e.g., `C:\dev\dll-library\Win11_23H2`).