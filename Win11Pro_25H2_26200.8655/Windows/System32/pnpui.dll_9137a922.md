# Binary Specification: pnpui.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\pnpui.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `9137a9222c999871ffeda55bb9ea7571649b5e272619736c3a0e275418953acd`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `InstallSecurityPrompt` | `0x3310` | 811 | UnwindData |  |
| 5 | `SimplifiedDINotificationW` | `0x3BB0` | 14,768 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `InstallSecurityPromptLUA` | `0x7560` | 1,588 | UnwindData |  |
| 3 | `InstallSecurityPromptRunDllW` | `0x7BA0` | 1,018 | UnwindData |  |
| 4 | `NotifyDevicesNeedRebootRunDllW` | `0xD470` | 179 | UnwindData |  |
| 6 | `DllCanUnloadNow` | `0xDCA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `DllGetClassObject` | `0xDCC0` | 174 | UnwindData |  |
