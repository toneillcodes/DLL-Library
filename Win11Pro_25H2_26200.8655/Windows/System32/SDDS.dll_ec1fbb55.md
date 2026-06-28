# Binary Specification: SDDS.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\SDDS.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `ec1fbb55cba01225465ee9480ee6940966f691e2773644865ab12f29ba5a6f5b`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0xA420` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0xA440` | 1,536 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `SDDSCreateChxDictionary` | `0xAA40` | 147 | UnwindData |  |
| 4 | `SDDSGetCharacterMappingObject` | `0xAAE0` | 282 | UnwindData |  |
