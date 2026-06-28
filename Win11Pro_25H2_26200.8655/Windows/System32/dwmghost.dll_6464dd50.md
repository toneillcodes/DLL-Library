# Binary Specification: dwmghost.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\dwmghost.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `6464dd50a669093574bb17266cb441c036188878e7f8ade6c9ff19c2df2e2f17`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DWMGhostCleanup` | `0x8B90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DWMGhostInitialize` | `0x8BA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DWMGhostSetInShutdown` | `0x8BB0` | 10,640 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DWMGhostHandleGhostMsg` | `0xB540` | 323 | UnwindData |  |
