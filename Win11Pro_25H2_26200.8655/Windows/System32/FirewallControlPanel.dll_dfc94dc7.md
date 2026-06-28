# Binary Specification: FirewallControlPanel.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\FirewallControlPanel.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `dfc94dc73268fce04badef145c86784150d875b12cfd3d1b55058beac1cfb1e8`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `DllRegisterServer` | `0xA790` | 4,048 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0xA790` | 4,048 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DllCanUnloadNow` | `0xB760` | 58 | UnwindData |  |
| 2 | `DllGetClassObject` | `0xB7A0` | 176 | UnwindData |  |
| 5 | `ShowNotificationDialogW` | `0xB9C0` | 1,448 | UnwindData |  |
| 6 | `ShowWarningDialogW` | `0xBF70` | 391 | UnwindData |  |
