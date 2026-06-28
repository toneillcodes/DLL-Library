# Binary Specification: AppVScripting.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\AppVScripting.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `5fded5db883ac50d3730eb7ae1eea35b27222e7247cf15b5348f94d0ce0b66f8`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `Deinitialize` | `0xE4A0` | 335 | UnwindData |  |
| 4 | `GetComponent` | `0xE600` | 248 | UnwindData |  |
| 1 | `Initialize` | `0xE700` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `InitializeISV` | `0xE710` | 111,228 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
