# Binary Specification: keymgr.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\keymgr.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `9e752e636ecf08c8b67226b49711864ee126d238304aedf6c83c39cd0e1735a9`
* **Total Exported Functions:** 10

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `DllCanUnloadNow` | `0x2470` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllGetClassObject` | `0x2490` | 162 | UnwindData |  |
| 1 | `CPlApplet` | `0x35C0` | 189 | UnwindData |  |
| 4 | `DllMain` | `0x36E0` | 116 | UnwindData |  |
| 5 | `KRShowKeyMgr` | `0x3760` | 291 | UnwindData |  |
| 6 | `PRShowRestoreFromMsginaW` | `0x8200` | 50 | UnwindData |  |
| 7 | `PRShowRestoreWizardExW` | `0x8200` | 50 | UnwindData |  |
| 8 | `PRShowRestoreWizardW` | `0x8240` | 875 | UnwindData |  |
| 9 | `PRShowSaveFromMsginaW` | `0x85C0` | 68 | UnwindData |  |
| 10 | `PRShowSaveWizardExW` | `0x8610` | 125 | UnwindData |  |
