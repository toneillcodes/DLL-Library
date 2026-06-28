# Binary Specification: dwmghost.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\dwmghost.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `c4627b58550d0b2d4c058e2a86e122b559d277527f20e88cb2406505fdfe5a3e`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DWMGhostCleanup` | `0x8B80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DWMGhostInitialize` | `0x8B90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DWMGhostSetInShutdown` | `0x8BA0` | 10,640 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DWMGhostHandleGhostMsg` | `0xB530` | 323 | UnwindData |  |
