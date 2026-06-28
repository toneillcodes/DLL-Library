# Binary Specification: Windows.UI.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\Windows.UI.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `4725e310bacf4330c0d8488a879aa6ccb7a7b92f0ffcb1facf33eefd52555916`
* **Total Exported Functions:** 15

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1500 | *Ordinal Only* | `0x125C0` | 1,084 | UnwindData |  |
| 1600 | *Ordinal Only* | `0x14860` | 42 | UnwindData |  |
| 1603 | `CreateControlInputEx` | `0x14890` | 57 | UnwindData |  |
| 1502 | `DllGetActivationFactory` | `0x232F0` | 852 | UnwindData |  |
| 1503 | `DllGetClassObject` | `0x2A3C0` | 408 | UnwindData |  |
| 1501 | `DllCanUnloadNow` | `0x42E30` | 121 | UnwindData |  |
| 1504 | `DllRegisterServer` | `0x69720` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1505 | `DllUnregisterServer` | `0x69750` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1506 | `GetWindowFromWindowId` | `0x69780` | 11,856 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1507 | `GetWindowIdFromWindow` | `0x69780` | 11,856 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1800 | *Ordinal Only* | `0x6C5D0` | 527 | UnwindData |  |
| 1602 | *Ordinal Only* | `0x6C7F0` | 56 | UnwindData |  |
| 1604 | *Ordinal Only* | `0x6C830` | 56 | UnwindData |  |
| 1601 | `CreateControlInput` | `0x6EB00` | 52 | UnwindData |  |
| 1700 | *Ordinal Only* | `0x84030` | 204 | UnwindData |  |
