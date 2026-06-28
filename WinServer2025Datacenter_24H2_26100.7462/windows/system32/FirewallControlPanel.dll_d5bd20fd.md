# Binary Specification: FirewallControlPanel.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\FirewallControlPanel.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d5bd20fd8e2be53bd798d398ea2452b36c7d5388abd2331cbceaa246872f8168`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `DllRegisterServer` | `0xA780` | 4,048 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0xA780` | 4,048 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DllCanUnloadNow` | `0xB750` | 58 | UnwindData |  |
| 2 | `DllGetClassObject` | `0xB790` | 176 | UnwindData |  |
| 5 | `ShowNotificationDialogW` | `0xB9B0` | 1,448 | UnwindData |  |
| 6 | `ShowWarningDialogW` | `0xBF60` | 391 | UnwindData |  |
