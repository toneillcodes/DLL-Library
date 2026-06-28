# Binary Specification: elsTrans.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\elsTrans.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `dd18edbec1b133e8db1a10cf79cf9c84b8e3539d3139f7530f4a60640407ce8c`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 6 | `RecognizeText` | `0x1010` | 143 | UnwindData |  |
| 2 | `EnumServices` | `0x1C00` | 94 | UnwindData |  |
| 3 | `FreePropertyBag` | `0x2E60` | 103 | UnwindData |  |
| 5 | `InitService` | `0x32B0` | 96 | UnwindData |  |
| 1 | `DoAction` | `0x4010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `FreeService` | `0x4020` | 1,056 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
