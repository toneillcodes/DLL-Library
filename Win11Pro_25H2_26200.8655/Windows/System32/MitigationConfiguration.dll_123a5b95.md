# Binary Specification: MitigationConfiguration.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\MitigationConfiguration.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `123a5b95acb7d8aaa45c130d46ab204b037d7acb9d1b96c1e09007cd07d4d5ec`
* **Total Exported Functions:** 8

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `DllRegisterServer` | `0x5C00` | 6,272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0x5C00` | 6,272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DllCanUnloadNow` | `0x7480` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x74A0` | 162 | UnwindData |  |
| 5 | `ExportMitigation` | `0xA0A0` | 1,673 | UnwindData |  |
| 6 | `ImportMitigation` | `0xA730` | 20,075 | UnwindData |  |
| 7 | `ValidateXML` | `0xF6A0` | 534 | UnwindData |  |
| 8 | `ValidateXMLFromManaged` | `0xF8C0` | 85 | UnwindData |  |
