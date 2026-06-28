# Binary Specification: MitigationConfiguration.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\MitigationConfiguration.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `74178dc0cdff09abc144c231cabfd001b45f9223da5d074b6115caadd32614bd`
* **Total Exported Functions:** 8

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `DllRegisterServer` | `0x5BF0` | 6,272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0x5BF0` | 6,272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DllCanUnloadNow` | `0x7470` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x7490` | 162 | UnwindData |  |
| 5 | `ExportMitigation` | `0xA090` | 1,673 | UnwindData |  |
| 6 | `ImportMitigation` | `0xA720` | 20,075 | UnwindData |  |
| 7 | `ValidateXML` | `0xF690` | 534 | UnwindData |  |
| 8 | `ValidateXMLFromManaged` | `0xF8B0` | 85 | UnwindData |  |
