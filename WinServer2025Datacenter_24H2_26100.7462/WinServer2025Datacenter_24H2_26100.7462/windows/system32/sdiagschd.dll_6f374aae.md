# Binary Specification: sdiagschd.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\sdiagschd.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `6f374aae1e3b2216b4668dfc3287dec4e8506242fa06b90b31562e4c432222fd`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x7560` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x7580` | 249 | UnwindData |  |
| 3 | `EnableScheduledDiagnostics` | `0x76E0` | 292 | UnwindData |  |
| 4 | `GetScheduledDiagnosticsExecutionLevel` | `0x7810` | 197 | UnwindData |  |
