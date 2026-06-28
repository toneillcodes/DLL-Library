# Binary Specification: netplwiz.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\netplwiz.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `3b394c6adc85e8c71bd0a1ca98cce4bafff02e0adb39d5affbda4e7952d462af`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 6 | `SHDisconnectNetDrives` | `0xC080` | 154 | UnwindData |  |
| 2 | `DllCanUnloadNow` | `0xC860` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllGetClassObject` | `0xC880` | 26 | UnwindData |  |
| 1 | `ClearAutoLogon` | `0xDF90` | 130 | UnwindData |  |
| 5 | `NetPlacesWizardDoModal` | `0x10980` | 587 | UnwindData |  |
| 4 | `NetAccessWizard` | `0x15E70` | 860 | UnwindData |  |
| 7 | `UsersRunDllW` | `0x19060` | 911 | UnwindData |  |
