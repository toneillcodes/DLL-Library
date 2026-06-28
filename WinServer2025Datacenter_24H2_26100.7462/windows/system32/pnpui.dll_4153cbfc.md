# Binary Specification: pnpui.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\pnpui.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `4153cbfc349690ee79898091351737ad7c41225c95ef110fb14b517f5694dafd`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `InstallSecurityPrompt` | `0x3300` | 811 | UnwindData |  |
| 5 | `SimplifiedDINotificationW` | `0x3BA0` | 14,736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `InstallSecurityPromptLUA` | `0x7530` | 1,588 | UnwindData |  |
| 3 | `InstallSecurityPromptRunDllW` | `0x7B70` | 1,018 | UnwindData |  |
| 4 | `NotifyDevicesNeedRebootRunDllW` | `0xD360` | 179 | UnwindData |  |
| 6 | `DllCanUnloadNow` | `0xDB90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `DllGetClassObject` | `0xDBB0` | 174 | UnwindData |  |
