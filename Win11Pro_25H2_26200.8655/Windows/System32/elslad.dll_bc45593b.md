# Binary Specification: elslad.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\elslad.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `bc45593b8abaadfb41fc9556d8efe3a7fa8229b4b7eaf89526256ec1df17fbd9`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `FreePropertyBag` | `0x2150` | 361 | UnwindData |  |
| 5 | `RecognizeText` | `0x22C0` | 800 | UnwindData |  |
| 4 | `InitService` | `0x3D30` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `FreeService` | `0x3DB0` | 90 | UnwindData |  |
| 1 | `DoAction` | `0x4E70` | 2,576 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
