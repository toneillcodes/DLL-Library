# Binary Specification: mimofcodec.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\mimofcodec.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `f5c9cddaa768120fcdab651a7c2cb3852894e1b7b55af041a8e38643bf6f37cd`
* **Total Exported Functions:** 8

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `MI_MOFParser_Delete` | `0x1BD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `MI_MOFParser_Init` | `0x1BE0` | 81 | UnwindData |  |
| 5 | `MI_MOFParser_Lex` | `0x1C40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `MI_MOFParser_Parse` | `0x1C50` | 54 | UnwindData |  |
| 1 | `MI_Application_NewDeserializer_Mof` | `0x28C0` | 101 | UnwindData |  |
| 2 | `MI_Application_NewSerializer_Mof` | `0x3320` | 205 | UnwindData |  |
| 8 | `NITS_STUB` | `0x16140` | 74,720 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `NITS_PRESENCE_STUB` | `0x28520` | 0 | Indeterminate |  |
