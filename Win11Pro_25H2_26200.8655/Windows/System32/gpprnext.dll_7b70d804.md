# Binary Specification: gpprnext.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\gpprnext.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `7b70d80429710aced6c76ee940eb773c0cd8bb9ce5a7b6be4d5bc9673f8b2c7f`
* **Total Exported Functions:** 8

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x2300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x2310` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllMain` | `0x2330` | 370 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x24B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DllUnregisterServer` | `0x24C0` | 338 | UnwindData |  |
| 6 | `PrinterGenerateGroupPolicy` | `0x2F20` | 415 | UnwindData |  |
| 7 | `PrinterProcessGroupPolicy` | `0x30D0` | 71 | UnwindData |  |
| 8 | `PrinterProcessGroupPolicyEx` | `0x3120` | 359 | UnwindData |  |
